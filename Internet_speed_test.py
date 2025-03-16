import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    print("Testing Download Speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    print("Testing Upload Speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    ping = st.results.ping

    print(f"\n📡 Internet Speed Test Results:")
    print(f"📥 Download Speed: {download_speed:.2f} Mbps")
    print(f"📤 Upload Speed: {upload_speed:.2f} Mbps")
    print(f"⏳ Ping: {ping:.2f} ms")

if __name__ == "__main__":
    test_speed()
