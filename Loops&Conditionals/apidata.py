api_responses = [200, 404, 500, 200, 201, 503, 200]

success_count = 0
client_error_count = 0
server_error_count = 0

for code in api_responses:
    if 200 <= code <= 299:
        success_count += 1
    elif 400 <= code <= 499:
        client_error_count += 1
    elif 500 <= code <= 599:
        server_error_count += 1

print("Total Success codes:", success_count)
print("Total Client Error codes:", client_error_count)
print("Total Server Error codes:", server_error_count)

