import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except ConnectionError:
            print("Connection to server lost.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '127.0.0.1'
    server_port = 8080

    try:
        client.connect((server_ip, server_port))
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        return

    #printing the message
    message = client.recv(1024).decode()
    print(message,end="")
    username = input()
    client.send(username.encode())

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    try:
        while True:
            message = input()
            client.send(message.encode())
            if message.lower() == 'exit':
                break
    except KeyboardInterrupt:
        print("Client disconnected.")
    finally:
        client.close()

if __name__ == "__main__":
    main()
