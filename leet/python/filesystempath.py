def max_path(path):
    struct_list = structure.split('\n')
    #now_depth = 0
    now_path = []
    max_path = ''
    for name in struct_list:
        bare_name = name.lstrip('\t')
        depth = (len(name) - len(bare_name))
        if depth >= len(now_path):
            now_path.append(bare_name)
        else:
            now_path[depth] = bare_name
        path = '/'.join(now_path[:depth+1])
        if len(path) > len(max_path):
            max_path = path
        print path
    return max_path



if __name__ == '__main__':
    structure = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\t\tkewei\n\t\t\t\tkewei2\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    print 'longest: ' + max_path(structure)
