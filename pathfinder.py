#!/usr/bin/env python3
import methods
from utils.Map import Map
from utils.Parser import parser

if __name__ == "__main__":
    args = parser()
    m = Map.gen_map(args.mapfile)
    methods.__dict__[args.method](m,args.start, args.end).run()
