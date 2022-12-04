# bilateral-filtering
**[EN]**
The bilateral filter aims to reduce noise while preserving the edges of objects in images. This filter applies two weights to each pixel in the image. The first is the intensity weight, which is related to the intensity value of the pixel. The second is the distance weight, which is related to the pixel's position. Thus, the values of other pixels that are similar to the color value of the pixel are predominantly summed, reducing the noise. However, it also tries to preserve the edges of objects in the image, taking into account the position of the pixel.

**[TR]**
Bilateral filter, görüntülerdeki nesnelerin kenarlarını korurken gürültüyü azaltmayı amaçlar. Bu filtre, görüntüdeki her piksele iki ayrı ağırlık değeri uygular. Birincisi, pikselin renk değeriyle ilgili olan renk ağırlığıdır. İkincisi ise, pikselin konumuyla ilgili olan mesafe ağırlığıdır. Böylece, pikselin renk değeri ile benzer olan diğer piksellerin değerleri ağırlıklı olarak toplanarak, gürültü azaltılır. Ancak, aynı zamanda pikselin konumu da dikkate alınarak, görüntüdeki nesnelerin kenarları da korunmaya çalışılır.

![image](https://user-images.githubusercontent.com/57074947/203318897-783db420-6d99-41a2-b129-6088486a687b.png)
