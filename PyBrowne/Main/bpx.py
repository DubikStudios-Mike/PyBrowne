# def addToString(variable, string):
#     variable = variable + string


# DOES NOT COMPLETELY WORK YET!

def run(item, type, mode):

    if type.lower().strip() == 'bpx':

        cache = ''
        cache2 = ''
        vars = ()
        var_vals = ()

        if mode == 'safe':
            itemAccess = 0
        elif mode == 'normal':
            itemAccess = 1
        else:
            itemAccess = 0

        with open(item, 'r+') as item:
            in_i = item.readlines()
            strin_i = str(in_i)
            strin_i.replace("'", '')
            strin_i.replace("]", '')
            strin_i.replace("[", '')
            strin_i.replace(",", '')


        for i in strin_i:
            cache = cache + str(i)
            if cache2 == 'w:':
                print(str(i))
            if '!0' in cache:
                print("Process terminated.")
                break
            elif 'w:' in cache:
                cache2 = 'w:'
            # print(cache + cache2)

# run('/home/justmike/workspaces/PyBrowne-0.1.0/PyBrowne/Programs/TEST.bpx', 'bpx', 'normal')
