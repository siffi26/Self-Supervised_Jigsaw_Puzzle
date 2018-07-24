import tensorflow as tf

flags = tf.app.flags

# General network setup
flags.DEFINE_string('mode', 'train', 'train or test')
flags.DEFINE_string('model', 'matrix_capsule', 'matrix_capsule or vector_capsule or alexnet')
flags.DEFINE_string('loss_type', 'spread', 'spread or margin or cross_entropy')

# hamming set
flags.DEFINE_boolean('generateHammingSet', False, 'Generate a new HammingSet')
flags.DEFINE_integer('hammingSetSize', 10, 'Hamming set size')
flags.DEFINE_string('selectionMethod', 'max', 'max or mean')
flags.DEFINE_string('hammingFileName', 'max_hamming_set_', 'Name of the file to be saved')

# jigsaw
flags.DEFINE_integer('numCrops', 9, 'The number of jigsaw-puzzle crops')
flags.DEFINE_integer('cellSize', 75, 'The dimensions of the jigsaw input')
flags.DEFINE_integer('tileSize', 64, 'The dimensions of the jigsaw input')
flags.DEFINE_integer('colorJitter', 2, 'Number of pixels for color jittering')
flags.DEFINE_integer('cropSize', 225, 'Size of the crop extracted from each input image')

# Matrix Capsule architecture
flags.DEFINE_boolean('use_bias', True, 'Adds bias to init capsules')
flags.DEFINE_boolean('use_BN', False, 'Adds BN before conv1 layer')
flags.DEFINE_boolean('add_coords', True, 'Adds capsule coordinations')
flags.DEFINE_boolean('grad_clip', False, 'Adds gradient clipping to get rid of exploding gradient')
flags.DEFINE_boolean('L2_reg', False, 'Adds L2-regularization to all the network weights')
flags.DEFINE_float('lmbda', 5e-04, 'L2-regularization coefficient')
flags.DEFINE_boolean('add_decoder', False, 'Adds a fully connected decoder and reconstruction loss')
flags.DEFINE_integer('iter', 1, 'Number of EM-routing iterations')
flags.DEFINE_integer('A', 32, 'A in Figure 1 of the paper')
flags.DEFINE_integer('B', 8, 'B in Figure 1 of the paper')
flags.DEFINE_integer('C', 16, 'C in Figure 1 of the paper')
flags.DEFINE_integer('D', 16, 'D in Figure 1 of the paper')
flags.DEFINE_integer('E', 16, 'E in Figure 1 of the paper')

# Training logs
flags.DEFINE_integer('max_epoch', 10000, 'maximum number of training epochs')
flags.DEFINE_integer('SUMMARY_FREQ', 100, 'Number of step to save summary')
flags.DEFINE_integer('VAL_FREQ', 1000, 'Number of step to evaluate the network on Validation data')

# Hyper-parameters
flags.DEFINE_integer('batchSize', 2, 'training batch size')
flags.DEFINE_integer('val_batch_size', 2, 'validation batch size')
flags.DEFINE_float('init_lr', 1e-3, 'Initial learning rate')
flags.DEFINE_float('lr_min', 1e-5, 'Minimum learning rate')

# data
flags.DEFINE_integer('N', 86380, 'Total number of training examples')
flags.DEFINE_string('data_path', './prepare_data/COCO_2017_unlabeled.h5', 'Data path')
flags.DEFINE_boolean('data_augment', True, 'Adds augmentation to data')
flags.DEFINE_integer('max_angle', 40, 'Maximum rotation angle along each axis; when applying augmentation')
flags.DEFINE_integer('height', 64, 'Input height size')
flags.DEFINE_integer('width', 64, 'Input width size')
flags.DEFINE_integer('depth', 32, 'Input depth size')
flags.DEFINE_integer('numChannels', 3, 'Input channel size')

# Directories and settings
flags.DEFINE_string('run_name', 'run01', 'Run name')
flags.DEFINE_string('logdir', './Results/log_dir/', 'Logs directory')
flags.DEFINE_string('modeldir', './Results/model_dir/', 'Saved models directory')
flags.DEFINE_string('savedir', './Results/result/', 'Results saving directory')
flags.DEFINE_string('model_name', 'model', 'Model file name')
flags.DEFINE_integer('reload_step', 0, 'Reload step to continue training')

args = tf.app.flags.FLAGS
