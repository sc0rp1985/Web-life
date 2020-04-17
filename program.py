from Life.LifeViewer import *
from Life.LifeGenerator import *
from Life.TurtleViewer import *
import time\


if __name__ == "__main__":

    world = LifeWorld.next_generation(10, "")
    dump = LifeWorld.get_dump_from_world(world);
    nextWorld = LifeWorld.next_generation(10, dump)

    str = ["0101010101", "0101000001111"]
    result = list(map(lambda x: list(map(int, x)), str))

    for i in str:
        a = int(i)

    dic = {}
    check_repeat = True
    world = LifeWorld(10, 10)
    # vm = input("select viewer: 0 - text, 1 - graphics\n")
    # if vm not in {'0', '1'}:
    #    raise Exception("error")

    #if self.ui.cbOutType.currentIndex() == 0:
    #    viewer = LifeViewer()
    #else:

    #viewer = TurtleViewer(800, 800)
    viewer = LifeViewer()

    while world.next_generation():
        if check_repeat:
            _hash = world.get_hash()
            val = dic.get(_hash)
            if val is None:
                dic[_hash] = world.get_generation()
            else:
                break
        viewer.show_world(world, False, '')
        #    viewer.show_world(world)
        time.sleep(0.05)

    legend = ''
    print("-------------COMPLETION OF EVOLUTION  {}-----------------".format(world.get_generation()))

    if world.get_empty():
        legend = "-------------EXTINCTION IN GENERATION {}-----------------".format(world.get_generation())
    else:
        _hash = world.get_hash()
        gen = dic.get(_hash)
        if gen is not None:
            if world.get_generation() - gen == 1:
                legend = "-------------STABLE CONFIGURATION IN GENERATION {}-----------------".format(gen)
            else:
                legend = "-------------REPEAT CONFIGURATION FROM GENERATION {}-----------------".format(gen)

    viewer.show_world(world, True, legend)
    print(legend)