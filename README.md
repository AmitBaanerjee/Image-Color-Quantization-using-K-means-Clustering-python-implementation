# Image-Color-Quantization-using-K-means-Clustering-python-implementation

Color quantization is the process of reducing the number of distinct colors used in an image. The main reason we may want to perform this kind of compression is to enable the rendering of an image in devices supporting only a limited number of colors (usually due to memory limitations).

Obviously all compressions come with a cost. In this case the resulting image may differ too much from the original one. Hence the goal of the color quantization is to obtain a compressed image as similar as possibile to the original one. The key factor for achieving this is the selection of the color palette by choosing the colors that most summarizes the original image.

The most common techniques reduce the problem of color quantization into a clustering problem of points where each point represents the color of a pixel. It consists in creating the palette by selecting a representative point for each cluster. After that the compression simply remaps all the colors into their cluster representative. As you may guess the resulting palette highly depends on the color space and distance metric used.

Before digging into the palette selection in more detail here's a simple and brief introduction about color spaces and color difference. The idea is to give a grasp on some concepts that are necessary to understand what comes next without being too much detailed as a more detailed explanation is out of the scope of this post. Feel free to skip these parts if you already know what they're talking about.

In this project I was given a input image of a baboon and the resultant quantized images using number of clusters(k), where k=3, k=5, k=10 and k=20 respectively;


 
