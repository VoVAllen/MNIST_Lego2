import argparse
from LegoGenerator import lego_generator, generate_component_settings
import numpy as np
from Component import generate_component
from img_util import ComponentSetting
from digit_coordinate import digit_coordinate_list

parser = argparse.ArgumentParser()
parser.add_argument("--componentnum", default=2)
parser.add_argument("--exportdir", default="")
# parser.add_argument("--numxclass", default="10x10")
# parser.add_help("")
args = parser.parse_args()
print 111
# num, num_class = args.numxclass.split("x")
num, num_class = 100, 1000
coordinates = digit_coordinate_list(num_class)
settings = generate_component_settings(coordinates)
# lego_dataset,label,components_set = lego_generator(int(num), int(num_class),component_num=1,settings=settings)
# np.save(args.exportdir+"one_componentset.npy",components_set)
# np.save(args.exportdir+"one_dataset.npy",lego_dataset)
# np.save(args.exportdir+"one_label.npy",label)

# settings=np.load('one_componentset.npy')
settings = [ComponentSetting(*list(settings[i])) for i in range(len(settings))]
lego_dataset2, label2, components_set2 = lego_generator(int(num), int(num_class), component_num=1, settings=settings)
np.save(args.exportdir + "one80_componentset.npy", components_set2)
np.save(args.exportdir + "one80_dataset.npy", lego_dataset2)
np.save(args.exportdir + "one80_label.npy", label2)
