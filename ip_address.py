import re

def cidr_to_ip(cidr):
    ip_address = str(cidr.split('/')[0])
    cidr_block = str(cidr.split('/')[1])
    
    print("CIDR: " + cidr)
    
    subnet_mask(cidr_block)
    wildcard_mask(cidr_block)

    if is_valid_ip(ip_address):
        hosts = (32-int(cidr_block))
        print(f'Hosts: {hosts}')
    else:
        print(f'{ip_address} is an invalid IP address.')

def subnet_mask(args):
    network_address = ('1' * int(args))
    host_address = ('0' * (32-int(args)))
    bits = network_address + host_address
    first_octet = bits[:8]
    second_octet = bits[8:16]
    third_octet = bits[16:24]
    fourth_octet = bits[24:32]
    mask = first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet
    subnet_mask = str(int(first_octet,2)) + '.' + str(int(second_octet,2)) + '.' + str(int(third_octet,2)) + '.' + str(int(fourth_octet,2))
    print("Binary: " + mask)
    print("Subnet mask: "+ subnet_mask)

def subnet_mask(args):
    network_address = ('1' * int(args))
    host_address = ('0' * (32-int(args)))
    bits = network_address + host_address
    first_octet = bits[:8]
    second_octet = bits[8:16]
    third_octet = bits[16:24]
    fourth_octet = bits[24:32]
    mask = first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet
    subnet_mask = str(int(first_octet,2)) + '.' + str(int(second_octet,2)) + '.' + str(int(third_octet,2)) + '.' + str(int(fourth_octet,2))
    print("Binary: " + mask)
    print("Subnet mask: "+ subnet_mask)

def wildcard_mask(args):
    network_address = ('1' * int(args))
    host_address = ('0' * (32-int(args)))
    bits = network_address + host_address
    bits = bits.replace('0', '%temp%').replace('1', '0').replace('%temp%', '1')
    first_octet = bits[:8]
    second_octet = bits[8:16]
    third_octet = bits[16:24]
    fourth_octet = bits[24:32]
    mask = first_octet + '.' + second_octet + '.' + third_octet + '.' + fourth_octet
    wildcard_mask = str(int(first_octet,2)) + '.' + str(int(second_octet,2)) + '.' + str(int(third_octet,2)) + '.' + str(int(fourth_octet,2))
    print("Binary: " + mask)
    print("Subnet mask: "+ wildcard_mask)

def is_valid_ip(*args):
    regex = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", *args)
    return bool(regex) and all(map(lambda n: 0<=int(n)<=255, regex.groups()))

if __name__ == '__main__':
    cidr_to_ip("8.8.8.8/28")
    
