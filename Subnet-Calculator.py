import random
import sys

def subnet_calc():
    try:
        print("\n")
        
        # Verifica se o endereço de IP é válido
        while True:
            ip_address = input("Digite o endereço de IP: ")
            
            #Checking octets            
            ip_octets = ip_address.split('.')
                        
            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            
            else:
                print("\nO endereço de IP é inválido! Tente novamente!\n")
                continue
        
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        
        #Checking Subnet Mask validity
        while True:
            subnet_mask = input("Digite a máscara subnet: ")
            
            #Checking octets            
            mask_octets = subnet_mask.split('.')
            
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            
            else:
                print("\nA máscara subnet é inválida! Tente novamente!\n")
                continue

		 
        #Algoritmo para identificação subnet, baseado no IP e Mascara
        #Converter mascara para string binária
        mask_octets_binary = []
        
        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            
            mask_octets_binary.append(binary_octet.zfill(8))
                
        binary_mask = "".join(mask_octets_binary)
        
        # Contando os bits na mascara e calculando o numero de hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)
        
        wildcard_octets = []
        
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))
            
        wildcard_mask = ".".join(wildcard_octets)
        
        #Convertendo IP para string binária
        ip_octets_binary = []
        
        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            
            ip_octets_binary.append(binary_octet.zfill(8))
                
        binary_ip = "".join(ip_octets_binary)
    
        # Obtendo endereço de internet/broadcast a partir da string binária
        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        
        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        
        # Convertendo para decimal novamente
        net_ip_octets = []
        
        #range(0, 32, 8) = 0, 8, 16, 24
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)
        
        net_ip_address = []
        
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))
            
        network_address = ".".join(net_ip_address)
        
        bst_ip_octets = []
        
        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)
        
        bst_ip_address = []
        
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))
            
        broadcast_address = ".".join(bst_ip_address)
        
        # Resultados
        print("\n")
        print("Endereço de internet é: %s" % network_address)
        print("Endereço de Broadcast é: %s" % broadcast_address)
        print("Número válido de hosts por subnet: %s" % no_of_hosts)
        print("Mascara wildcard: %s" % wildcard_mask)
        print("Mascara de bits: %s" % no_of_ones)
        print("\n")
        

        # Gerando endereços de IP aleatórios na subnet
        while True:
            generate = input("Gerar endereço de IP aleatório a partir da subnet? (s/n)")
            
            if generate == "s":
                generated_ip = []
                
                # Obtem os endereços de IP disponíveis no range,
                # baseado na deferença entre o endereço de broadcast e endereço de internet
                for indexb, oct_bst in enumerate(bst_ip_address):
                    for indexn, oct_net in enumerate(net_ip_address):
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                generated_ip.append(oct_bst)
                            else:
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))
                
                # Endereço de IP gerado através da subnet
                y_iaddr = ".".join(generated_ip)
                
                print("Endereço de IP aleatório é: %s" % y_iaddr)
                print("\n")
                continue
                
            else:
                print("Ok, Programa finalizado!\n")
                break
        
    except KeyboardInterrupt:
        print("\n\nPrograma finalizado pelo usuário. Saindo...\n")
        sys.exit()

subnet_calc()