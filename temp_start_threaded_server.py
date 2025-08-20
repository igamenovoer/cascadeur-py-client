from cascadeur_client.server import health_exec_server_threaded as h
import time
h.start_server(port=31015)
print('[temp] server started on 31015')
# Keep alive briefly for test
for i in range(5):
    time.sleep(1)
print('[temp] exiting')
