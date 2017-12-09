<br>


Hello there !

<div id="container">
    <img src="https://travis-ci.org/tbhaxor/pynimations.svg?branch=master" align=center>
    This is an image
</div>

Hi !

#container {
    height:100px;
    line-height:100px;
}

#container img {
    vertical-align:middle;
    max-height:100%;
}
# Python Supported Versions
This module is supported with all python **3.x** 

# Dependencies
1. **pbars**, to install type "_`pip3 install pbars`_"

# Features
+ Customisable
+ Easy to use

# Downloading
_if you have pip3 added to enviroment variable_
```
pip3 install pynimations
```
# How to use
Note : Explaing any one of them, rest all is same
1. import `progressbar` from pynimations
```python
from pynimations import progressbar
```

2. create an instance of progressbar
```python
pb = progressbar()   # for arguments refer the following table
```

3. call animate method
```python
pb.animate()
```

# Argument Description for Animations
## 1.) rotator
<table>
<thead>
<tr>
<th>Argument</th>
<th align="center">Default Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>label</td>
<td align="center">Loading</td>
<td>Accepts a string - Used for giving an label (prefix text) of animator</td>
</tr>
<tr>
<td>interval</td>
<td align="center">100</td>
  <td>Accepts an positive integer - Used for animation delay interval (<i>in ms</i>)</td>
</tr>
<tr>
<td>iteration</td>
<td align="center">5</td>
<td>Accepts an positive integer - Used for looping whole animation iteration</td>
</tr></tbody></table>

## 2.) progressbar
<table>
<thead>
<tr>
<th>Argument</th>
<th align="center">Default Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>label</td>
<td align="center">Loading</td>
<td>Accepts a string - Used for giving an label (prefix text) of animator</td>
</tr>
<tr>
<td>interval</td>
<td align="center">100</td>
  <td>Accepts an positive integer - Used for animation delay interval (<i>in ms</i>)</td>
</tr>
<tr>
<td>length</td>
<td align="center">30</td>
<td>Accepts an positive integer - Used for deciding the width of progress bar</td>
</tr>
<tr>
<td>style</td>
<td align="center">pip</td>
<td>Accepts a string - Used for styling the progress bar</td>
</tr></tbody></table>



