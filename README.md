# Package name: image-processing-package
 
Projeto exemplo: processamento de imagem / Digital Innovation One
Autor(a): Karina Kato

O pacote "image-processing-package" contém a seguinte estrutura:

	- Módulo Processing:
		Histogram matching
		Structural similarity
		Resize image
		
	- Módulo Utils:
		Read image
		Save image
		Plot image
		Plot result
		Plot histogram

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

python -m pip install --upgrade pip

python -m pip install --user twine

python -m pip install --user setuptools

python setup.py sdist bdist_wheel

```bash
pip install package_name
```

## Usage
```python
from image_processing.utils import io, plot

from image_processing.processing import combination, transformation

image1 = io.read_image(path file1.jpg)

image2 = io.read_image(path file2.jpg)

plot.plot_image(image1)

plot.plot_image(image2)

result_image = combination.transfer_histogram(image1, image2)

plot.plot_result(image1, image2, result_image)


```

## License
[MIT](https://choosealicense.com/licenses/mit/)
