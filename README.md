# UNM Nuclear LaTeX Templates

## Description
This repository stores LaTeX templates developed for the University of New Mexico's Department of Nuclear Engineering.
These templates are developed for a multitude of purposes, including classes such **NE323L: Radiation Detection and Measurement**, **NE313L: Introduction to Laboratory Techniques for Nuclear Engineering**, and **NE413L: Nuclear Engineering Laboratory I**.
Templates will be created and edited as an ongoing basis, and will be subjected to periodic updates should they be seen fit.
Additional sections (such as a table of contents) are also included in the template, albeit commented-out as per the source provided.

## Software and Usage
LaTeX files can be compiled using many different IDEs such as [TexMaker](https://www.xm1math.net/texmaker/) and [PyCharm](https://www.jetbrains.com/pycharm/) [^pycharm], and it is ultimately up the user to determine what they are most comfortable using.
Alternatively, cloud-based compilers such as [Overleaf](https://overleaf.com) are popular options.
To compile on a local system, `pdflatex` will need to be installed from the [TeX Live](https://www.tug.org/texlive/) package.

## Instructions
### Preamble
For all templates provided, be sure to include the required class document (`.cls`) in the working directory, else the `PDF` will not be compiled.
### Compiling
To run the program as designed, a `.bbl` file will need to be generated in order for the `PDF` to be compiled correctly.
To do this, you will need to first compile with `pdflatex` to generate the `.aux` file.
Then, run `BibTeX` on the `.aux` file, which will generate the necessary `.bbl` file.
Recompile your document twice using `pdflatex` to ensure the bibliography is loaded correctly.
This process will need to be repeated if the bibliography file is updated and new citations are added to the document.
If citations change the order in which they appear, this process will also need to be repeated.

For a more streamlined process, `Makefiles` are in the process of being added to templates.
The use of these assumes the user has installed `TeXLive` and its associated packages.
Simply running `make` in a terminal will generate a `pdf`, while `make clean` will clean up the junk files created during compilation.
### Bibliography
A provided `references.bib` file is found in the repository, and the template is current set up to import this. 
Please feel free to add references as needed, following the steps above.
Citation managers such as [MyBib](https://www.mybib.com/), [Zotero](https://www.zotero.org/), and [Mendeley](https://www.mendeley.com/) can serve to format and store references until you are ready to insert them into your LaTeX document.
[Zotero](https://www.zotero.org/), in particular, is recommended because of its Firefox plugin for citing websites and for its `Better BibTeX` plugin, which automatically updates your `BibTeX` file in your working directory.

## Additional Notes
Adjust the `vspace` command in the .cls file to change the spacing in the heading for more desired formatting, particularly when the title is multiline.


## Support
For additional support first consult the omniscient [Google](https://www.google.com/).
If this fails, take a break and try again later.
If again this fails, email [Liam Pohlmann](lipohlmann@unm.edu).
AI *may* be able to help, but caution is urged.

## Licensing
This project and its contents are licensed under the **Glorious People's Licence** (**GPL**).
The software is distributed as-is, and the user assumes full responsibility for any issues that result from honest mistakes or sheer stupidity.

## Contributors and Acknowledgements
Primary author: [Liam Pohlmann](lipohlmann@unm.edu)

Contributions are welcomed and encouraged from all students.

## Updates
Further improvements will be made on an as-needed basis or as-desired basis.


[^pycharm]: The [TeXiFy-IDEA]https://plugins.jetbrains.com/plugin/9473-texify-idea) plugin will be required to use this IDE.
