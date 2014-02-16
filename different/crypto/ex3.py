import hmac

maker = hmac.new('secret_key'.encode())

with open('lorem.txt', 'rb') as file:
    while True:
        block = file.read(1024)
        if not block: break
        maker.update(block)

print(maker.hexdigest())
