#KarmaRunner for SublimeText

KarmaRunner provides an easy interface for running Karma directly from SublimeText editor.

The main features are:
- starting and stopping Karma from the drop-down menu
- shows Karma output pannel whenever it detects a ".js" file is saved

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

				// path to the location where karma.conf.js file is stored
				"path": "${project_path}/test/",
				"working_dir": "${project_path}/test/",

				// redirecting output to the SublimeANSI plugin
				// this plugin apply color to Karma output
				"syntax": "Packages/ANSIescape/ANSI.tmLanguage",
				"target": "ansi_color_build"
			}
		],
	}

##4. Configuring Karma to run Continuously
In your Karma config file you should set **singleRun** to **false** and **autoWatch** to **true**, so that Karma continuously watches for file changes. That way Karma will automatically re-run all the tests whenever it detects a JavaScript file was saved.

Here's a snippet from the Karma config file:

    // enable / disable watching file and executing tests whenever any file changes
    autoWatch: true,

    // Continuous Integration mode
    // if true, Karma captures browsers, runs the tests and exits
    singleRun: false,

##5. Configuring Karma to use colors (optional)
In order for Karma results to look better you need to use **spec** reporter. See the [karma-spec-reporter Git page](https://github.com/mlex/karma-spec-reporter) for instructions on how to install and set it up.

##6. Using
To run Karma simply choose **Tools > Karma > Run Karma** or press Ctrl+P and type "Run Karma"

To stop Karma choose **Tools > Karma > Kill Karma** or press Ctrl+P and type "Kill Karma"
