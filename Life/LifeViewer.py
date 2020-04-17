from Life.Viewer import AbstractViewer


class LifeViewer(AbstractViewer):

    @staticmethod
    def show_world(world,  fix_window, legend):
        if world.get_empty():
            print("**********AVERYBODY IS DEAD IN GENERATION {0}************".format(world.get_generation()))
            return
        _str = '--------------GENERATION {0}--------------\n'.format(world.get_generation())
        for row in world.get_world():
            for col in row:
                if col == 0:
                    _str = _str + '   '
                else:
                    _str = _str + ' # '
            _str = _str + '\n'
        print("\033[2J\033[1;1H" + _str)
