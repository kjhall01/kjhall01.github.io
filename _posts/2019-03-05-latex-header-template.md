---
layout: post
title: "Latex Header Template"
excerpt: "A convenient header file with a compilation of packages and example usages"
tags: [Latex]
comments: true
last_modified_at: 2019-03-05T14:00:00
---

<link rel="stylesheet" href="https://formden.com/static/assets/demos/bootstrap-iso/bootstrap-iso/bootstrap-iso.css">

To avoid creating the Latex header every time I start a project, I tend to keep a Latex header template file that I can reuse from project to project. Items that are included in this Latex header template are: 

- Various packages with comments for their usage;
- Predefined commands and acronyms;

You can edit this file from [here](https://github.com/Weiming-Hu/Weiming-Hu.github.io/blob/master/_posts/2019-03-05-latex-header-template.md) if you have the proper permission.

<script>
function copyText() {
  /* Get the text field */
  var copyText = document.getElementsByClassName("highlight");

  var $temp = $("<textarea>");
  $("body").append($temp);
  $temp.val(copyText[0].innerText).select();
  document.execCommand("copy");
  $temp.remove();

  /* Alert the copied text */
  alert("Header contents are copied!");
}  
</script>

<div class="bootstrap-iso">
<button onclick="copyText()" type="button" class="btn btn-success">Copy header contents</button>
</div>

```
% Version number 0.4.4
% If you have made any changes, please consider also changing
% https://github.com/Weiming-Hu/Weiming-Hu.github.io/blob/master/_posts/2019-03-05-latex-header-template.md
%
% The MIT License (MIT)
% 
% Copyright (c) 2019 Weiming Hu
% 
% Permission is hereby granted, free of charge, to any person obtaining a copy
% of this software and associated documentation files (the "Software"), to deal
% in the Software without restriction, including without limitation the rights
% to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
% copies of the Software, and to permit persons to whom the Software is
% furnished to do so, subject to the following conditions:
% 
% The above copyright notice and this permission notice shall be included in all
% copies or substantial portions of the Software.
% 
% THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
% IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
% FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
% AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
% LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
% OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
% SOFTWARE.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                        Ready-to-Use Packages                             %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% For text colors
% A set of colors are predefined: black, blue, brown, cyan, darkgray, gray, green,
% lightgray, lime, magenta, olive, orange, pink, purple, red, teal, violet, white, yellow.
%
\usepackage{xcolor}

% For large chunks of comment
\usepackage{verbatim}

% Include packages
\usepackage{inputenc}

% For graphics and figures
\usepackage{graphicx}

% For math symbols
\usepackage{amssymb}

% To add line numbers, use the following package, and add
% \linenumbers
% before the text/section where you would like to include line numbers afterwards.
% 
% \usepackage{lineno}
% 
% If you do not want line numbers at each line, you can use the following code
% which only add line numbers every 5 lines.
% 
\usepackage[modulo]{lineno}
%
% If you want to further tweak how many lines between two line numbers, you can 
% specify the following when you are using the modulo argument.
%
\modulolinenumbers[2]

% Include the package to deal with breaking URLs
% 
% If you want to make the url to break at any character, use the following line
% \sloppy \url{long-long-long-url}
% 
% \usepackage[hyphenbreaks]{breakurl}
\usepackage[hyphens]{url}

% For tagged hyper-links
\usepackage[bookmarks, colorlinks, breaklinks, pdfauthor={Weiming Hu},unicode=true]{hyperref}

% For typesetting pseudo code
\usepackage{algorithm}
\usepackage[noend]{algpseudocode}

% Set up link format
\hypersetup{linkcolor=blue,citecolor=blue,filecolor=black}

% To change the layout and margins to A4 paper layout
% \usepackage[a4paper, total={6in, 8in}]{geometry}

% For nested itemized environment
\usepackage{outlines}

% Provide the degree symbol
\usepackage{textcomp}
\usepackage{gensymb}

% If you want to typeset chemical formula, use the following package
% \usepackage[version=4]{mhchem}
% and then use this in your writing
% \ce{H2SO4}

% For creating check boxes. Please read on to see how to create
% check boxes with symbols for being finished and broken.
%
% Include the package for enumerating items
\usepackage{enumitem}

% Include the pacakage for the proceeding symbols before each item
\usepackage{amssymb}

% Include the package for accessing the post script standard symbol
\usepackage{pifont}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                            Bibliography                                  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% For bibliography, please choose ONE from the following
%
% To use natbib (which is stable and widely accepted but old),
% uncomment the following line.
%
\usepackage[numbers]{natbib}
%
% Put the following two lines in your tex file where you want
% to create the bibliography (usually at the end before the end
% of the document environment).
%
% \bibliographystyle{plainnat}
% \bibliography{your-bib-file.bib}
%

% To use biblatex (which is new and powerful but might not
% be compatible with some journals), uncomment the following line.
%
% \usepackage{biblatex}
%
% Put the following line before your document environment
% (also called the preamble)
%
% \addbibresource{your-bib-file.bib}
%
% And put the following where you want to create the bibliography
% (usually at the end before the end of the document environment).
%
% \printbibliography
%
% If you want the bib to be included in the table of content, you
% can instead use the following option.
%
% \printbibliography[heading=bibintoc,title={References}]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                             To-Do List                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Create an environment for the to-do list and some relevant symbols
\newlist{todo}{itemize}{2}
\setlist[todo]{label=$\square$}
\newcommand{\cmark}{\ding{51}}%
\newcommand{\xmark}{\ding{55}}%
\newcommand{\done}{\rlap{$\square$}{\raisebox{2pt}{\large\hspace{1pt}\cmark}}%
\hspace{-2.5pt}}
\newcommand{\wontfix}{\rlap{$\square$}{\large\hspace{1pt}\xmark}}

% To create a to-do list, please use the following method
%
% \begin{todo}
%   \item[\done] This is done.
%   \item This has yet to be done.
%   \item[\wontfix] This is broken.
% \end{todo}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                    Header File Customization                             %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% For customized header file
%
% You can comment this out if you are using the common header file.
% This package gives you the possibilities to create a customized
% header file. Read more if you want to create a customized front page
%
% \usepackage{ragged2e}
% 
% Use the following snippets as examples to create customized font page
% inside the document environment
% \setlength{\parskip}{12.0pt}
% \begin{Center}
% {\fontsize{20pt}{24.0pt}\selectfont \textbf{Weiming Hu}\par}
% \end{Center}\par
% \begin{Center}
% {\fontsize{20pt}{24.0pt}\selectfont Candidate for the Ph.D. degree in Geography \\
% The Pennsylvania State University\par}
% \end{Center}\par
% \vspace{\baselineskip}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                    Subfigures and Subtables                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% The package subfigure has been obsolete. Looks like the package subcaption has
% been gaining some popularity. So the example is using this package.
%
% http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/caption/subcaption.pdf
%

% \usepackage{caption}
% \usepackage{subcaption}

% Set the caption width to be a little bit smaller than the text width.
% \captionsetup[sub]{width=0.8\textwidth}

% \begin{figure}
%     \begin{minipage}[t]{0.5\textwidth}
%         \centering
%         \includegraphics[width=\textwidth]{figure1}
%         \subcaption{caption1}
%         \label{fig:label1}
%   \end{minipage}
%   \begin{minipage}[t]{0.5\textwidth}
%         \centering
%         \includegraphics[width=\textwidth]{figure2}
%         \subcaption{caption2}
%         \label{fig:label2}
%     \end{minipage}
% \end{figure}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                Acronyms                                  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Documentation URL for package glossaries
% http://tug.ctan.org/macros/latex/contrib/glossaries/glossariesbegin.pdf
% 
% Documentation URL for Glossary styles
% https://www.dickimaw-books.com/gallery/glossaries-styles/
% 
% Add acronyms without appearing in the table of content
% \usepackage[acronym]{glossaries}

% By default, glossaries will appear as chapters if the document class
% features the \chapter command and as sections otherwise. You can change
% the default behavior using the section key-value-option; e.g.,
% 
\usepackage[toc, section=section, acronym]{glossaries}
\usepackage[toc, section=section]{glossaries}

%\usepackage{glossaries-extra-stylemods}
%\usepackage{glossary-longbooktabs}
%\usepackage{glossaries-extra}
%\usepackage{glossary-inline}
\usepackage{glossary-mcols}

% If you are specifying acronym for package glossaries,
% use this to automatically spell out the acronym when 
% first used so you do not need to keep track of them.
%
\setacronymstyle{long-short}
%\setabbreviationstyle{long-short}

% Choose a style. You can access all available styles 
% using the URL for GLossary styles.
%
% \setglossarystyle{inline}
% \setglossarystyle{index}
\setglossarystyle{mcolindex}

% Topic: Models and Techniques
\newacronym{GFS}{GFS}{Global Forecast System}
\newacronym{GEFS}{GEFS}{Global Ensemble Forecast System}
\newacronym{ECMWF}{ECMWF}{European Center for Medium Weather Forecasting}
\newacronym{AnEn}{AnEn}{Analog Ensemble}
\newacronym{PAnEn}{PAnEn}{Parallel Analog Ensemble}
\newacronym{NWP}{NWP}{Numerical Weather Prediction}
\newacronym{PAN}{PAN}{Persistence Analog}
\newacronym{GCM}{GCM}{General Circulation Model}
\newacronym{NAM}{NAM}{North American Mesoscale Model}
\newacronym{WRF}{WRF}{Weather Research and Forecasting}
\newacronym{SSE}{SSE}{Search Space Extension}
\newacronym{EA}{EA}{Evolutionary Analog}
\newacronym{GA}{GA}{Genetic Algorithm}
\newacronym{KF}{KF}{Kalman Filter}
\newacronym{CRM}{CRM}{Cloud Resolving Models}
\newacronym{HRRR}{HRRR}{High-Resolution Rapid Refresh}
\newacronym{SAM}{SAM}{System Advisor Model}
\newacronym{HF}{HF}{Heuristic Filter}
\newacronym{LOO}{LOO}{Leave-One-Out}
\newacronym{SS}{SS}{Schaake Shuffle}
\newacronym{SSI}{SSI}{Spectral Statistical Interpolation}
\newacronym{GSI}{GSI}{Gridpoint Statistical Interpolation}
\newacronym{UMAP}{UMAP}{Uniform Manifold Approximation and Projection}
\newacronym{SOM}{SOM}{Self-Organizing Map}


% Topic: Organizations and Projects
\newacronym{NCEP}{NCEP}{National Centers for Environmental Prediction}
\newacronym{WU}{WU}{Weather Underground}
\newacronym{PWS}{PWS}{Private Weather Station}
\newacronym{NOAA}{NOAA}{National Oceanic and Atmospheric Agency}
\newacronym{WHO}{WHO}{World Health Organization}
\newacronym{ATSDR}{ATSDR}{Agency for Toxic Substances and Diseases Registry}
\newacronym{CMIP}{CMIP}{Coupled Model Intercomparison Project}
\newacronym{IPCC}{IPCC}{International Panel on Climate Change}
\newacronym{ASOS}{ASOS}{Automated Surface Observing System}
\newacronym{NCAR}{NCAR}{National Center for Atmospheric Research}
\newacronym{GISS}{GISS}{Goddard Institute for Space Studies}
\newacronym{RCP}{RCP}{Representative Concentration Pathway}
\newacronym{WRCP}{WRCP}{World Climate Research Programme}

% Topic: Metrics
\newacronym{SVI}{SVI}{Social Vulnerability Index}
\newacronym{ME}{ME}{Mean Error}
\newacronym{RMSE}{RMSE}{Root Mean Square Error}
\newacronym{CRMSE}{CRMSE}{Centered Root Mean Square Error}
\newacronym{RC}{RC}{Rank Correlation}
\newacronym{MSE}{MSE}{Mean Square Error}
\newacronym{OMT}{OMT}{Over Max Time}
\newacronym{CRPS}{CRPS}{Continuous Rank Probability Score}
\newacronym{RPS}{RPS}{Rank Probability Score}
\newacronym{MAE}{MAE}{Mean Absolute Error}
\newacronym{Brier}{Brier}{Brier Score}

% Topic: Renewables
\newacronym{PV}{PV}{Photovoltaic}
\newacronym{AVS}{AVS}{Agrivoltaic System}
\newacronym{LBR}{LBR}{Land-Based Renewables}
\newacronym{USSE}{USSE}{Utility-Scale Solar Energy}

% Topic: miscellaneous
\newacronym{VGI}{VGI}{Volunteered Geographic Information}
\newacronym{UHI}{UHI}{Urban Heat Island}
\newacronym{CONUS}{CONUS}{Continental United States}

% Topic: Math
\newacronym{IDW}{IDW}{Inverse Distance Weighted}
\newacronym{PDF}{PDF}{Probability Distribution Function}
\newacronym{CDF}{CDF}{Cumulative Distribution Function}

% Topic: Computer Science
\newacronym{API}{API}{Application Programming Interface}
\newacronym{PEF}{PEF}{Parallel Ensemble Program}
\newacronym{CLI}{CLI}{Command Line Interface}
\newacronym{RAM}{RAM}{Random Access Memory}
\newacronym{UML}{UML}{Unified Modeling Language}
\newacronym{TAU}{TAU}{Tuning and Analysis Utilities}
\newacronym{HPC}{HPC}{High-Performance Computing}
\newacronym{ANN}{ANN}{Artifitial Neural Network}
\newacronym{ML}{ML}{Machine Learning}

% Topic: Meteorology
\newcommand*{\elnino}{El Ni\~no }
\newacronym{FLT}{FLT}{Forecast Lead Time}
\newacronym{ITCZ}{ITCZ}{Intertropical Convergence Zone}
\newacronym{ENSO}{ENSO}{El Ni\~no Southern Oscillation}
\newacronym{PDO}{PDO}{Pacific Decadal Oscillation}
\newacronym{MOS}{MOS}{Model Output Statistics}
\newacronym{PNA}{PNA}{Pacific/North American}
\newacronym{GHG}{GHG}{Greenhouse gas}


% To include glossary in the document, keep the following first line,
% and add the second line into your document where you would
% like the glossary to be inserted.
% \makeglossaries
% \printglossaries


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                        Command Definitions                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Define commands that come in handy
\newcommand*{\Fig}[1]{Figure~\ref{#1}}
\newcommand*{\Figs}[1]{Figures~\ref{#1}}
\newcommand*{\Table}[1]{Table~\ref{#1}}
\newcommand*{\Tables}[1]{Tables~\ref{#1}}
\newcommand*{\Eqr}[1]{(\ref{#1})}
\newcommand*{\Eq}[1]{Equation~(\ref{#1})}
\newcommand*{\Eqs}[1]{Equations~(\ref{#1})}
\newcommand*{\Sect}[1]{Section~\ref{#1}}
\newcommand*{\Sects}[1]{Sections~\ref{#1}}
\newcommand*{\Alg}[1]{Algorithm~\ref{#1}}

% Commands for providing notes, comments, ...
\newcommand*{\weimingNote}[1]{\textbf{\textcolor{red}{#1}}}

% If you have made any changes, please consider also changing
% https://github.com/Weiming-Hu/Weiming-Hu.github.io/blob/master/_posts/2019-03-05-latex-header-template.md
%

% THE END

```
