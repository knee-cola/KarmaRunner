#KarmaRunner for SublimeText

KarmaRunner provides a easy interface for running Karma directly from SublimeText editor.

The main features are:
- starting and stopping Karma from the drop-down menu
- blocks the Esc button from closing the build results pannel (where the Karma outputs it's results)

![KarmaRunner Screenshot](https://raw.githubusercontent.com/knee-cola/KarmaRunner/master/KarmaRunnerScreenshot.PNG)


##1. Prerequisites
Before installing KarmaRunner make sure to install [SublimeANSI](https://github.com/aziz/SublimeANSI).

Also you need to install and configure the [Karma test runner](https://www.npmjs.com/package/karma) and make sure it works as expected.

##2. Installation

You can install via [Sublime Package Control](http://wbond.net/sublime_packages/package_control)
Or you can clone this repository into your SublimeText Packages directory
    
##3. Build System Settings

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

##4. Using
To run Karma simply choose **Tools > Karma > Run Karma** or press Ctrl+P and type "Run Karma"

To stop Karma choose **Tools > Karma > Kill Karma** or press Ctrl+P and type "Kill Karma"
