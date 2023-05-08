# SSORT-Semantic-Segmentation-for-Off-Road-Traversability
Compilation of state of the art architectures such as DeepLabV3, FCN, SegFormer and Segment Anything Model (SAM) on off-road dataset along with it's deployment.

# Datasets
## Yamaha-CMU
Yamaha-CMU-Off-Road, or YCOR, which consists of 1076 images collected in four different locations in Western Pennsylvania and Ohio, spanning three different seasons.
The dataset was labelled using a polygon-based interface with eight classes: sky, rough trail, smooth trail, traversable grass, high vegetation, non-traversable low vegetation, obstacle. The polygon labels were post-processed using a Dense CRF to densify the labels; the output of the CRF was manually inspected, and in some cases corrected, to ensure no wrong labels were created. [Link](https://theairlab.org/yamaha-offroad-dataset/)
## RUGD : Robot Unstructured Ground Driving 
The RUGD dataset focuses on semantic understanding of unstructured outdoor environments for applications in off-road autonomous navigation. The datset is comprised of video sequences captured from the camera onboard a mobile robot platform. The overall goal of the data collection is to provide a more representative dataset of environments that lack structural cues that are commonly found in urban city autonmous navigation datasets. The platform used for data collection is small enough to manuever in cluttered environments, and is rugged enough to traverse through challenging terrain to explore more unstructured areas of an environment.
[Link](http://rugd.vision/)

# Models
## DeepLabV3
[DeepLabv3](https://arxiv.org/abs/1706.05587v3) is a semantic segmentation architecture that improves upon DeepLabv2 with several modifications. To handle the problem of segmenting objects at multiple scales, modules are designed which employ atrous convolution in cascade or in parallel to capture multi-scale context by adopting multiple atrous rates. Furthermore, the Atrous Spatial Pyramid Pooling module from DeepLabv2 augmented with image-level features encoding global context and further boost performance.
## FCN
[Fully Convolutional Networks](https://arxiv.org/abs/1605.06211v1), or FCNs, are an architecture used mainly for semantic segmentation. They employ solely locally connected layers, such as convolution, pooling and upsampling. Avoiding the use of dense layers means less parameters (making the networks faster to train). It also means an FCN can work for variable image sizes given all connections are local.
The network consists of a downsampling path, used to extract and interpret the context, and an upsampling path, which allows for localization.
FCNs also employ skip connections to recover the fine-grained spatial information lost in the downsampling path.
## SegFormer
[SegFormer](https://arxiv.org/pdf/2105.15203v3.pdf), a simple, efficient yet powerful semantic segmentation framework which unifies Transformers with lightweight multilayer perception (MLP) decoders. SegFormer has two appealing features: 1) SegFormer comprises a novel hierarchically structured Transformer encoder which outputs multiscale features. It does not need positional encoding, thereby avoiding the interpolation of positional codes which leads to decreased performance when the testing resolution differs from training. 2) SegFormer avoids complex decoders. The proposed MLP decoder aggregates information from different layers, and thus combining both local attention and global attention to render powerful representations. 
This simple and lightweight design is the key to efficient segmentation on Transformers.
## Segment Anything Model (SAM)
[SAM](https://arxiv.org/abs/2304.02643) has learned a general notion of what objects are – this understanding enables
zero-shot generalization to unfamiliar objects and images without requiring additional train-
ing.SAM’s advanced capabilities are the result of its training on millions of images and masks
collected through the use of a model-in-the-loop ”data engine.” Researchers used SAM and
its data to interactively annotate images and update the model. This cycle was repeated
many times over to improve both the model and the dataset.


# Start
To start the backend, just run:
```
$ python server.py
template/index.html
```
All instances should run on seperate posts.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
