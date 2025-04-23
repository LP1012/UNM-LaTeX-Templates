%! Class = CLASS_NAME
%! Author = lipohlmann
%! Date = 08/24/23

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{juniorlabs}

\LoadClass[a4paper,11pt]{article}

% Very necessary packages
\RequirePackage[margin=1in]{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{abstract}
\RequirePackage{pdfpages}
\RequirePackage{setspace}
\RequirePackage{mathtools}
\RequirePackage{graphicx}
\RequirePackage{hyperref}
\RequirePackage{parskip} % This rempves all indentations in the report.
\RequirePackage{sectsty}
\RequirePackage{authblk}
\RequirePackage{footmisc}
\RequirePackage[labelfont=bf]{caption}

\RequirePackage{subcaption} % writing captions for subfigures

\RequirePackage[explicit]{titlesec}

% Equation stuff
\RequirePackage{bm}
\RequirePackage{amsmath}
\RequirePackage{amsfonts} % fonts for math
\RequirePackage{amssymb}
\RequirePackage{amsbsy}
\RequirePackage[bbgreekl]{mathbbol} % not really sure what this does...
\DeclareSymbolFontAlphabet{\mathbbl}{bbold}
\RequirePackage{bbm, dsfont}

%\RequirePackage{minted} % This little sh*t might cause issues
%\RequirePackage{xcolor}
%\definecolor{LightGray}{gray}{0.95}

% Random packages that may (or may not) come in handy
\RequirePackage{acro}
\RequirePackage{algorithm,algpseudocode}
\RequirePackage{arydshln} % draw dashed lines in tables
\RequirePackage{multirow}
\RequirePackage{stmaryrd} % for computer symbols...
\RequirePackage{xspace}
\RequirePackage{url}
\RequirePackage{verbatim} % `minted` should be used for code
\RequirePackage{rotating}
\RequirePackage{booktabs} % makes tables look prettier
\RequirePackage[noprefix]{nomencl}  % for nomenclature
\RequirePackage{float} % improves interface for float objects like tables
\RequirePackage{newtxtext}
\RequirePackage{nicefrac}

% Packages I think are worthwile:
\RequirePackage[inkscapeformat=png]{svg}
\RequirePackage{wrapfig} % Creates wrapped images in text. Don't use with equations!
\RequirePackage{tikz}
\RequirePackage{adjustbox}
\RequirePackage{tablefootnote}
\RequirePackage{csvsimple} % Turns csv's into tables
\RequirePackage{booktabs} % Helps csvsimple package
\RequirePackage[super]{nth} % Creates superscrips for ordinal numbers
\RequirePackage{soul} % strikethrough text

% ---------------------------------------------------------------------------- %
% Fix table numbering
\renewcommand{\thetable}{\Roman{table}}

\renewcommand{\UrlFont}{\normalfont}

% ---------------------------------------------------------------------------- %
% Hyperlink setup
\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=magenta,
    urlcolor=black,
    citecolor=black
}

% ---------------------------------------------------------------------------- %
\renewcommand{\headrulewidth}{0pt}
\pagestyle{fancy}
\fancyhf{}
\setlength{\headheight}{20pt} % might need to make this 20pt...

% ---------------------------------------------------------------------------- %
% Treatment of floats
\renewcommand{\topfraction}{0.85}       % max fraction of floats at top
\renewcommand{\textfraction}{0.1}       % allow minimal text w. figs
\renewcommand{\floatpagefraction}{0.7}  % require fuller float pages
\floatplacement{figure}{H}

% ---------------------------------------------------------------------------- %
% Sections
\titleformat{\section}{\fontsize{11}{14}\normalfont\bfseries}{\thesection}{1em}{\MakeUppercase{#1}}\sectionfont{\MakeUppercase}
\titleformat{\subsection}{\fontsize{11}{14}\normalfont\bfseries}{\thesubsection}{1em}{#1}
\titleformat{\subsubsection}{\fontsize{11}{14}\normalfont\bfseries}{\thesubsubsection}{1em}{#1}

% ---------------------------------------------------------------------------- %
% Subtitle of document
\newcommand\subtitle[1]{\renewcommand\@subtitle{\itshape #1}} % Apply \itshape to make it italicized
\newcommand\@subtitle{}

% ---------------------------------------------------------------------------- %
% Pretty sure these next ones need to be specified.
\renewcommand{\abstractname}{ABSTRACT}
\renewenvironment{abstract}
{\begin{center}
     \normalfont\bfseries \abstractname
\end{center}
    \list{}{\leftmargin1cm \rightmargin\leftmargin}%
    \item\relax\itshape}
        \endlist

        \newenvironment{keywords}
        {\begin{center}
             \normalfont\bfseries KEYWORDS
        \end{center}
            \list{}{\leftmargin1cm \rightmargin\leftmargin}
            \item\relax\itshape\centering
            }
                \endlist

\renewcommand{\contentsname}{CONTENTS}
\renewcommand{\listfigurename}{FIGURES}
\renewcommand{\listtablename}{TABLES}

% ---------------------------------------------------------------------------- %
% Fix Footnotes
\newcommand{\@paperheading}{
    \thispagestyle{empty}
    \begin{center}
        \vbox to 0.5in{%
                {\fontfamily{ptm}\fontsize{14}{18}\selectfont\bfseries{\strut\MakeUppercase{\@title}\par}}
                {\fontfamily{ptm}\fontsize{12}{16}\selectfont{\@subtitle\par}}
        }
        \vspace{28pt}
    \end{center}
}
\newcommand{\@addauthors}{
    \begin{center}
        \vbox to 1.4in{
            \bgroup
            \fontfamily{ptm}\fontsize{11}{12}\selectfont % Set font size for authors
            \renewcommand*\Authfont{\fontfamily{ptm}\fontsize{11}{12}\bfseries}
            \renewcommand*\Affilfont{\fontfamily{ptm}\fontsize{11}{12}\itshape}

            % Authors (displayed on the same line)
            {\centering \@author \@thanks}

            \vspace{10pt} % Adjust the vertical space between authors and affiliations

            % Email Addresses
            \@email
            \vspace{17pt}
            \egroup
        }
    \end{center}
}

\newcommand{\email}[1]{\gdef\@email{\centering\itshape {#1}}}

% ---------------------------------------------------------------------------- %
% This creates the heading...
\newcommand{\ReportHeading}{\bgroup
\parindent=0pt
\@paperheading
\@addauthors
}

