// Timer variables
let timeLeft = 25 * 60;
let isRunning = false;
let isPaused = false;
let worker;

// DOM elements
const timerDisplay = document.getElementById('timer-display');
const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const beepSound = document.getElementById('beepSound');

// Create Web Worker for accurate timing
function createWorker() {
    const workerCode = `
        let interval;
        self.onmessage = function(e) {
            if (e.data.command === 'start') {
                interval = setInterval(() => {
                    postMessage('tick');
                }, 1000);
            } else if (e.data.command === 'stop') {
                clearInterval(interval);
            }
        };
    `;
    const blob = new Blob([workerCode], { type: 'application/javascript' });
    return new Worker(URL.createObjectURL(blob));
}

function updateTimerDisplay() {
    const minutes = String(Math.floor(timeLeft / 60)).padStart(2, '0');
    const seconds = String(timeLeft % 60).padStart(2, '0');
    timerDisplay.textContent = `${minutes}:${seconds}`;
    document.title = `⏳ ${minutes}:${seconds} Pomodoro Timer`;
}

function startTimer() {
    if (isRunning && !isPaused) return;
    
    const inputMinutes = parseInt(document.getElementById('work').value);
    if (isNaN(inputMinutes) || inputMinutes <= 0) return;

    // Initialize or restart worker
    if (!worker) {
        worker = createWorker();
        worker.onmessage = function(e) {
            if (e.data === 'tick' && !isPaused) {
                if (timeLeft > 0) {
                    timeLeft--;
                    updateTimerDisplay();
                } else {
                    timerComplete();
                }
            }
        };
    }

    if (!isRunning || isPaused) {
        timeLeft = inputMinutes * 60;
        updateTimerDisplay();
        isRunning = true;
        isPaused = false;
        worker.postMessage({ command: 'start' });
    }
}

function stopTimer() {
    if (isRunning) {
        isPaused = !isPaused;
        stopBtn.textContent = isPaused ? "▶️ Resume" : "⏸️ Pause";
        if (isPaused) {
            worker.postMessage({ command: 'stop' });
        document.title = "⏸️ Paused - Pomodoro Timer";
        } else {
            worker.postMessage({ command: 'start' });
        }
    }
}

function timerComplete() {
    if (worker) {
        worker.postMessage({ command: 'stop' });
    }
    isRunning = false;
    document.title = "✅ Pomodoro Done!";
    beepSound.play();
    // Optional: Show notification if tab is inactive
    if (document.hidden) {
        showNotification("Pomodoro Timer", "Time is up!");
    }
}

function showNotification(title, message) {
    if (!("Notification" in window)) return;
    
    if (Notification.permission === "granted") {
        new Notification(title, { body: message });
    } else if (Notification.permission !== "denied") {
        Notification.requestPermission().then(permission => {
            if (permission === "granted") {
                new Notification(title, { body: message });
            }
        });
    }
}

// Clean up worker when page unloads
window.addEventListener('beforeunload', function() {
    if (worker) {
        worker.terminate();
    }
});

// Initialize
startBtn.addEventListener('click', () => {
    stopBtn.textContent = "⏸️ Pause";
    startTimer();
});
stopBtn.addEventListener('click', stopTimer);
updateTimerDisplay();

// Dark Mode Toggle (unchanged)
const darkToggle = document.getElementById('darkModeToggle');
darkToggle.addEventListener('change', function () {
    document.body.classList.toggle('dark-mode');
    document.querySelectorAll('.card, .form-control, .btn, .list-group-item').forEach(el => {
        el.classList.toggle('dark-mode');
    });
});
// ... (keep all the timer and Web Worker code from previous solution)

// Task management with enhanced UI feedback
document.getElementById("task-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const taskInput = document.getElementById("task-input");
    const task = taskInput.value.trim();

    if (!task) return;

    fetch("/add_task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ task })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const li = document.createElement("li");
            li.className = "list-group-item d-flex justify-content-between align-items-center";
            li.innerHTML = `
                <span class="task-text">${task}</span>
                <div>
                    <button name="complete_task" value="${data.index}" class="btn btn-outline-success btn-sm complete-btn">✓ Done</button>
                    <button name="delete_task" value="${data.index}" class="btn btn-outline-danger btn-sm delete-btn">🗑️ Delete</button>
                </div>
            `;
            document.getElementById("task-list").appendChild(li);
            taskInput.value = "";
        }
    });
});

// Enhanced task completion and deletion
document.addEventListener('click', function(e) {
    // Complete task - strike through text
    if (e.target && e.target.classList.contains('complete-btn')) {
        e.preventDefault();
        const index = e.target.value;
        const taskItem = e.target.closest('li');
        const taskText = taskItem.querySelector('.task-text');
        
        // Visual feedback immediately
        taskText.style.textDecoration = 'line-through';
        taskText.style.opacity = '0.7';
        e.target.disabled = true;
        
        fetch("/complete_task", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ index })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                // Optional: Remove after delay or keep as completed
                setTimeout(() => {
                    taskItem.remove();
                }, 1000);
            } else {
                // Revert if failed
                taskText.style.textDecoration = 'none';
                taskText.style.opacity = '1';
                e.target.disabled = false;
            }
        });
    }
    
    // Delete task - slide out animation
    if (e.target && e.target.classList.contains('delete-btn')) {
        e.preventDefault();
        const index = e.target.value;
        const taskItem = e.target.closest('li');
        
        // Visual feedback immediately
        taskItem.style.transform = 'translateX(-100%)';
        taskItem.style.opacity = '0';
        taskItem.style.transition = 'all 0.3s ease';
        
        fetch("/delete_task", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ index })
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                // Remove after animation completes
                setTimeout(() => {
                    taskItem.remove();
                }, 300);
            } else {
                // Revert if failed
                taskItem.style.transform = 'translateX(0)';
                taskItem.style.opacity = '1';
            }
        });
    }
});

// Load existing tasks with proper styling
document.addEventListener('DOMContentLoaded', function() {
    fetch("/")
    .then(response => response.text())
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const taskList = doc.getElementById('task-list');
        if (taskList) {
            document.getElementById('task-list').innerHTML = taskList.innerHTML;
            
            // Apply completed task styling for any pre-existing completed tasks
            document.querySelectorAll('#task-list li').forEach(item => {
                if (item.querySelector('form button[name="complete_task"]')) {
                    const completeBtn = item.querySelector('form button[name="complete_task"]');
                    if (completeBtn.disabled) {
                        const taskText = item.querySelector('.task-text') || item.querySelector('span');
                        if (taskText) {
                            taskText.style.textDecoration = 'line-through';
                            taskText.style.opacity = '0.7';
                        }
                    }
                }
            });
        }
    });
});