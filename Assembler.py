# Assembler v0.1
class Assembler:
    def __init__(self, in_file,out_file):
        #Call Praser functions here
        try:
            self.R_parser(in_file,out_file)
        except ValueError:
            print('Error occurrs!')
    #R-type parser function
    def R_parser(self,in_file,out_file):
        f = open(in_file, 'r') #read .asm file
        o = open(out_file,'w+')
        opCode = '000000'
        registers_map = {
            '$0': '00000',
            '$at': '00001',
            '$v0': '00010',
            '$v1': '00011',
            '$a0': '00100',
            '$a1': '00101',
            '$a2': '00110',
            '$a3': '00111',
            '$t0': '01000',
            '$t1': '01001',
            '$t2': '01010',
            '$t3': '01011',
            '$t4': '01100',
            '$t5': '01101',
            '$t6': '01110',
            '$t7': '01111',
            '$s0': '10000',
            '$s1': '10001',
            '$s2': '10010',
            '$s3': '10011',
            '$s4': '10100',
            '$s5': '10101',
            '$s6': '10110',
            '$s7': '10111',
            '$t8': '11000',
            '$t9': '11001',
            '$k0': '11010',
            '$k1': '11011',
            '$gp': '11100',
            '$sp': '11101',
            '$fp': '11110',
            '$ra': '11111'
        }
        func_map = {'add': '100000', 'sub': '100010', 'and': '100100',
                    'or': '100101', 'slt': '101010', 'sll': '000000', 'srl': '000010'}
        if f.mode == 'r':
            f = f.readlines()
            for line in f:
                func = line[0:line.find(" ")]
                registers = line[line.find(" ")+1:len(line)].split(',')
                if(func == 'sll' or func == 'srl'):
                    registers = {
                        'rs': '00000', 'shamt': '{0:05b}'.format(int(registers[2])), 'rd': registers[0], 'rt': registers[1]}
                    instruction = '{}{}{}{}{}{}'.format(
                        opCode,  registers['rs'], registers_map[registers['rt']], registers_map[registers['rd']], registers['shamt'], func_map[func])
                else:
                    registers = {
                        'rs': registers[1], 'rt': registers[2], 'rd': registers[0], 'shamt': '00000'}
                    instruction = '{}{}{}{}{}{}'.format(
                        opCode,  registers_map[registers['rs']], registers_map[registers['rt']], registers_map[registers['rd']], registers['shamt'], func_map[func])

                o.write(instruction+'\n')


def main():
    file = 'mips1.asm'
    out = 'out.txt'
    assembler = Assembler(file,out)


if __name__ == '__main__':
    main()