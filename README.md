# Research-and-Development-of-methods-for-recovering-document-illumination

Made by team NovieOPI - Stanisalv Ushakov, Kamil Alyakaev.

# Instructions

There are four yaml files with configurations of the necessary environments, run:

<code> conda env create --name envname --file=environment_name.yml </code>

The structure of the datasets in the disk is identical to the one that is in the project <code> Dataset </code> folder

Scripts have a number of options:
  1. **type** - the type of the model we use, either <code> classic or cropped </code>, for test scripts inside the model the option <code> mixed </code> is also avaliable
  2. **model** - the name of the model to be used - <code> SG, STGAN or SF </code>
  3. **size** - resultion of the input test data - <code> low, medium or full </code>
  4. **results** - the results folder that would be used - <code> classic, cropped or mixed </code>

# Links
Pretrained [weights](https://disk.yandex.com/d/k-5UzQQk75zF2Q)

Used [datasets](https://disk.yandex.com/d/uyfjBuNNsy1Jxg)

Archive [datasets](https://disk.yandex.com/d/bHY_F6nrjLndEQ)
