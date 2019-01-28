##
# .release.sdistutils - distutils data
##
"""
Python distutils data module.

This module exists in the case that someone wants to sub-package a distribution
as opposed to relying on install-time dependency resolution.

For sub-packagers, the `prefixed_packages` and `prefixed_extensions` functions
should be of particular interest.
"""
import sys
import os
import distutils.core
from .. import project
from . import pypi

subpackages = [
	'bin',
	'test',
	'documentation',
	'release',
]

extensions_data = {
	'lib' : {
		'sources' : [],
	},
}

package_data = {
	'documentation' : ['*.rst'],
	'documentation.sphinx' : ['*.sh', '*.py'],
	None : ['*.c'],
}

if __package__ is not None:
	default_prefix = __package__.split('.')[:-1]
else:
	default_prefix = __name__.split('.')[:-2]

def prefixed_extensions(
	prefix = default_prefix,
	extensions_data = extensions_data,
):
	"""
	Generator producing the `distutils` `Extension` objects.
	"""
	pkg_prefix = '.'.join(prefix) + '.'
	path_prefix = os.path.sep.join(prefix)
	for mod, data in extensions_data.items():
		yield distutils.core.Extension(
			pkg_prefix + mod,
			[os.path.join(path_prefix, src) for src in data['sources']],
			libraries = data.get('libraries', ()),
		)

def prefixed_packages(
	prefix = default_prefix,
	packages = subpackages,
):
	"""
	Generator producing the standard `package` list prefixed with `prefix`.
	"""
	prefix = '.'.join(prefix)
	yield prefix
	prefix = prefix + '.'
	for pkg in packages:
		yield prefix + pkg

def prefixed_package_data(
	prefix = default_prefix,
	package_data = package_data,
):
	"""
	Generator producing the standard `package` list prefixed with `prefix`.
	"""
	prefix = '.'.join(prefix)
	for pkg, data in package_data.items():
		if pkg is None:
			yield prefix, data
		else:
			yield prefix + '.' + pkg, data

def standard_setup_keywords(build_extensions = True, prefix = default_prefix):
	return {
		'name' : project.name,
		'version' : project.version,
		'description' : project.abstract,
		'author' : project.meaculpa,
		'author_email' : project.contact,
		'url' : pypi.URL,
		'classifiers' : pypi.CLASSIFIERS,
		'long_description' : pypi.LONG_DESCRIPTION,
		'packages' : list(prefixed_packages(prefix = prefix)),
		'package_data' : dict(prefixed_package_data(prefix = prefix)),
		#'ext_modules' : list(prefixed_extensions(prefix = prefix)),
	}
