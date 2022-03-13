const eleventyNavigationPlugin = require("@11ty/eleventy-navigation");
// const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function(eleventyConfig) {

    eleventyConfig.addPassthroughCopy({"static/css": "css"});
    eleventyConfig.addWatchTarget("static/css");
    eleventyConfig.addPassthroughCopy({"static/js": "js"});
    eleventyConfig.addWatchTarget("static/js");
    eleventyConfig.addPlugin(eleventyNavigationPlugin);
    // eleventyConfig.addPlugin(syntaxHighlight);

    return {
        dir: {
            input: "src",
            output: "_site",
            includes: "_includes"
        }
    }
}

