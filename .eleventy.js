module.exports = function(eleventyConfig) {

    eleventyConfig.addWatchTarget("./src/css/");
    eleventyConfig.addPassthroughCopy("./src/css/");
    eleventyConfig.addWatchTarget("./src/js/");
    eleventyConfig.addPassthroughCopy("./src/js/");

    return {
        dir: {
            input: "src",
            output: "_site",
            includes: "_includes"
        }
    }
};