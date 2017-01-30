#KarmaRunner for SublimeText

KarmaRunner provides a easy interface for running Karma directly from SublimeText editor.

The main features are:
- starting and stopping Karma from the drop-down menu
- disables the Escape buttin closing the build results pannel (where the Karma outputs it's results)

##1. Prerequisites
Before installing KarmaRunner make sure to install [SublimeANSI](https://github.com/aziz/SublimeANSI).

##2. Installation

    npm install -g karmarunner
    
##3. Additional settings

KarmaRunner needs a build system to be setup in the Sublime's project file.
The default name for the build system is "Karma" (can be overriden in plugin settings file).
Here's an example:

    {
    	"build_systems":
    	[
		    {
    			"name": "Karma",
			"cmd":
				[
					"C:\\Program Files (x86)\\nodejs\\node.exe",
					"node_modules/karma/bin/karma",
					"start",
					"karma.conf.js"
				],
				"path": "${project_path}/test/",
				"syntax": "Packages/ANSIescape/ANSI.tmLanguage",
				"target": "ansi_color_build",
				"working_dir": "${project_path}/test/"
			}
		],
	}