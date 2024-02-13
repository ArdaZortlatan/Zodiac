import socket
import ipaddress

def check_ports(ip, ports, show_closed_ports=True):
    open_ports = []

    for port in ports:
        if check_port(ip, port):
            open_ports.append(port)

    if open_ports:
        print(f"IP: {ip}, Açık: {open_ports}")
    elif show_closed_ports:
        print(f"IP: {ip}, Kapalı: {ports}")

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)  # Timeout süresini ayarlayabilirsiniz

    try:
        sock.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

def main():
    try:
        print("""
__________         .___.__                 
\____    /____   __| _/|__|____    ____    
  /     //  _ \ / __ | |  \__  \ _/ ___\   
 /     /(  <_> ) /_/ | |  |/ __ \\  \___   
/_______ \____/\____ | |__(____  /\___  >  
        \/          \/         \/     \/   
Created by: ArdaZortlatan                                           
                                           
                                           
                                           
                                           
                                           
""")
        start_ip = ipaddress.IPv4Address(input("Başlangıç IPv4'ü girin: "))
        end_ip = ipaddress.IPv4Address(input("Bitiş IPv4'ü girin: "))
        port_str = input("Kontrol edilecek port numaralarını virgülle ayırarak girin (örneğin: 21,80,442): ")
        ports = [int(p.strip()) for p in port_str.split(',')]
        show_closed_ports = input("Kapalı portları da gösterilsin mi? (Evet için 'e', Hayır için 'h'): ").lower() == 'e'
    except ValueError:
        print("Hatalı giriş! Lütfen doğru formatta giriş yapın.")
        return

    if start_ip > end_ip:
        print("Başlangıç IP'si, bitiş IP'sinden büyük olmalıdır.")
        return

    print(f"Belirlenen aralıkta {start_ip} ile {end_ip} arasındaki IP adreslerinin {ports} portlarını kontrol ediliyor...")

    for ip_int in range(int(start_ip), int(end_ip) + 1):
        current_ip = ipaddress.IPv4Address(ip_int)
        current_ip_str = str(current_ip)
        check_ports(current_ip_str, ports, show_closed_ports)

    input("Programı kapatmak için Enter tuşuna basın...")

if __name__ == "__main__":
    main()