# NE323L Labs
To use this template, simply copy over the `.tex`, `.bib`, `.cls`, and `Makefile` to a working directory of your choosing. 
If (when) you rename your `.tex` file, be sure to rename the `manuscript` variable in the `Makefile` to reflect your new name.
The `Makefile` will automatically find your `.bib` file should you create your own or rename.
Just make sure it is correctly referenced in your `.tex` file.
To generate a `PDF`, open a terminal and type `make`, then click `Enter`.
You will notice a lot of additional files are created.
**This is expected**.
To get rid of this, simply type `make clean`, then hit `Enter`.
Other functionalities exist in the `Makefile` should anyone be interested.
Type `make realclean` to get rid of *everything*, including the created `PDF` (will not delete your `.tex` file.

## Tips
- Write your sections in separate documents, then include them in your main `.tex` document using `\include{filename}`. This will keep your `.tex` file cleaner. See `general_hw/report_style` for an example of this.
- Always start a new line in LaTeX for a new sentence. Trust me -- it makes your code much easier to read.
- Use Zotero to create to your bibliography. Look up BetterBibTeX plugin for Zotero and the Firefox/Chrome browser extension for Zotero. The former will auto-update your `.bib` file as you add citations, while the latter will auto-cite web pages and papers by just clicking the button!

