def base32_encode(data):
    # Define the base32 alphabet
    base32_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

    # Convert input data to bytes
    if isinstance(data, str):
        data = data.encode()

    # Initialize variables
    result = []
    buffer = 0
    bits_remaining = 0

    # Iterate through each byte in the data
    for byte in data:
        buffer = (buffer << 8) | byte
        bits_remaining += 8

        # Process the buffer while there are at least 5 bits remaining
        while bits_remaining >= 5:
            bits_remaining -= 5
            index = (buffer >> bits_remaining) & 0x1F
            result.append(base32_alphabet[index])

    # Handle remaining bits in the buffer
    if bits_remaining > 0:
        buffer <<= (5 - bits_remaining)
        index = buffer & 0x1F
        result.append(base32_alphabet[index])

    # Pad the result with '=' characters if necessary (to make the length a multiple of 8)
    padding_length = (8 - len(result) % 8) % 8
    result.extend(['='] * padding_length)

    # Join the result list into a string and return
    return ''.join(result)

def base32_decode(encoded_data):
    # Define the base32 alphabet
    base32_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

    # Convert input data to uppercase (in case of lowercase input)
    encoded_data = encoded_data.upper()

    # Remove any padding characters from the end
    if '=' in encoded_data:
        encoded_data = encoded_data[:encoded_data.index('=')]

    # Initialize variables
    result = bytearray()
    buffer = 0
    bits_remaining = 0

    # Iterate through each character in the encoded data
    for char in encoded_data:
        if char not in base32_alphabet:
            raise ValueError("Invalid base32 character")

        # Find the index of the character in the base32 alphabet
        index = base32_alphabet.index(char)

        # Add the bits to the buffer
        buffer = (buffer << 5) | index
        bits_remaining += 5

        # Extract bytes from the buffer while there are at least 8 bits available
        while bits_remaining >= 8:
            bits_remaining -= 8
            result.append((buffer >> bits_remaining) & 0xFF)

    # Return the decoded data as a bytes object
    return bytes(result)
