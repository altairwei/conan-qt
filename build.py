#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager
import copy

if __name__ == "__main__":
    extra_options = {
        "qt:qtsvg": "True", 
        "qt:qttools": "True", 
        "qt:qttranslations": "True", 
        "qt:qtimageformats": "True", 
        "qt:qtgraphicaleffects": "True", 
        "qt:qtwebsockets": "True",
        "qt:qtwebchannel": "True",
        "qt:qtwebengine":"True"
    }
    #TODO: add upload url
    builder = ConanMultiPackager(
        username="altairwei",
        upload = "https://api.bintray.com/conan/altairwei/conan",
        remotes= "https://api.bintray.com/conan/bincrafters/public-conan, https://api.bintray.com/conan/conan-community/conan",
        archs = ["x86_64"])
    builder.add_common_builds(pure_c=False)
    # Add extra options to common builds
    extra_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        new_options = copy.deepcopy(options)
        new_options.update(extra_options)
        extra_builds.append((
            copy.deepcopy(settings), 
            new_options, 
            copy.deepcopy(env_vars), 
            copy.deepcopy(build_requires), 
            copy.deepcopy(reference)))

    builder.builds += extra_builds
    builder.run()
