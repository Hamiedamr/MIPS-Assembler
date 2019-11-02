# Assembler v0.1.1
class Assembler:
    def __init__(self, in_file, out_file):
        # Call Praser functions here
        f = open(in_file, 'r')  # read .asm file
        f = f.readlines()
        o = open(out_file, 'a')
        o.truncate(0)
        o = open(out_file, 'a')
        self.registers_map = {
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
        self.func_map = {
            'and': '100100',
            'sll': '000000',
            'add': '100000',
            'or': '100101‬',
            'jr': '001000',
            'slt': '101010'
        }
        self.i_map = {
            'sw':  '101011',
            'lw':  '100011',
            'beq': '000100',
            'addi': '001000',
            'ori': '001101'
        }
        try:

            for line in f:
                line = line.replace("\n", "")
                op = line[0:line.find(" ")]
                if op in self.func_map.keys():
                    self.R_parser(line, o)
                elif op in self.i_map.keys():
                    self.I_parser(line, o)
                else:
                    self.J_parser(line, o)

        except ValueError:
            print('Error occurrs!')
    # R-type parser function

    def R_parser(self, line, o):
        opCode = '000000'
        func = line[0:line.find(" ")]
        registers = line[line.find(" ")+1:len(line)].split(',')
        if(func == 'sll'):
            registers = {
                'rs': '00000', 'shamt': '{0:05b}'.format(int(registers[2])), 'rd': registers[0], 'rt': registers[1]}
            instruction = '{}{}{}{}{}{}'.format(
                opCode,  registers['rs'], self.registers_map[registers['rt']], self.registers_map[registers['rd']], registers['shamt'], self.func_map[func])
        else:
            registers = {
                'rs': registers[1], 'rt': registers[2], 'rd': registers[0], 'shamt': '00000'}
            instruction = '{}{}{}{}{}{}'.format(opCode,  self.registers_map[registers['rs']], self.registers_map[
                                                registers['rt']], self.registers_map[registers['rd']], registers['shamt'], self.func_map[func])
        o.write(instruction+'\n')

    def I_parser(self, line, o):
        func = line[0:line.find(" ")]
        if func != 'sw' and func != 'lw':
            registers = line[line.find(" ")+1:len(line)].split(',')
            registers = {'rs': registers[0], 'rt': registers[1],
                         'val': '{0:016b}'.format(int(registers[2]))}
            instruction = '{}{}{}{}'.format(
                self.i_map[func],  self.registers_map[registers['rt']], self.registers_map[registers['rs']], registers['val'])
        else:
            registers = line[line.find(" ")+1:len(line)].split(',')
            registers.append([x[0:x.find('(')] for x in registers][1])
            registers[1] = [x[x.find('$'):x.find(')')] for x in registers][1]
            registers = {'rt': registers[0], 'rs': registers[1], 'val': '{0:016b}'.format(
                int(registers[2]))}
            instruction = '{}{}{}{}'.format(
                self.i_map[func],  self.registers_map[registers['rs']], self.registers_map[registers['rt']], registers['val'])

        o.write(instruction+'\n')

    def J_parser(self, line, o):
        pass


def main():
    file = 'mips1.asm'
    out = 'out.txt'
    assembler = Assembler(file, out)


if __name__ == '__main__':
    main()
