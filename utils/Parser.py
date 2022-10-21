from argparse import ArgumentParser

def parser():
    argparser =  ArgumentParser()
    argparser.add_argument("mapfile")
    argparser.add_argument("method")
    argparser.add_argument("start",type=int,nargs=2)
    argparser.add_argument("end",type=int,nargs=2)
    args = argparser.parse_args()
    args.start = tuple(args.start)
    args.end = tuple(args.end)
    return args