network_address = input("network address:").split('.')
N = int(input("Num of networks: "))
nets = {}
for i in range(1,N+1):
    print("Network ",i,":" , end='')
    nets[i] = int(input())

new_nets =sorted(nets.items(), key=lambda x: x[1],reverse=True)
last = 0
typ = 2
if typ == 1:
    for i,e in enumerate(new_nets):
        power = 0
        num = 0
        while num - 2 < e[1]:
            power += 1
            num = 2 ** power
        
        last_item = (8-power) * "1" + (power) * "0"
        subnet_num = int(last_item,2)
        network_address[3] = last + 1
        last += num
        print("network " + str(e[0]) + ":")
        print("first address:",network_address[0] + "." + network_address[1] + "." +network_address[2] + "." + str(network_address[3]))
        print("subnet:","255.255.255."+str(subnet_num))
        print()
        #print(subnet_num)
else:
    net_size = 0
    last = int(network_address[3])
    for i,e in enumerate(new_nets):
        power = 0
        num = 0
        while num - 2 < e[1]:
            power += 1
            num = 2 ** power
        if power > 8:
            last_item = '00000000'
            last2_item = (8 - (power - 8)) * "1" + (power-8) * "0"
        else:
            last_item = (8-power) * "1" + (power) * "0"
            last2_item = '11111111'
    
        
        subnet_num = int(last_item,2)
        subnet_num_last2 = int(last2_item,2)
        network_address[3] = last + 1
        last += num
        if last > 255:
            network_address[2] = str( int(network_address[2])+1)
            network_address[3] = last - 255
            last = last - 255

        print("network " + str(e[0]) + ":")
        print("first address:",network_address[0] + "." + network_address[1] + "." +network_address[2] + "." + str(network_address[3]))

        print("last usable address:",network_address[0] + "." + network_address[1] + "." +network_address[2] + "." + str(network_address[3] + num - 3))
        print("brodcast address:",network_address[0] + "." + network_address[1] + "." +network_address[2] + "." + str(network_address[3] + num - 2))
        
        print("subnet:","255.255."+str(subnet_num_last2)+"."+str(subnet_num))
        print()


