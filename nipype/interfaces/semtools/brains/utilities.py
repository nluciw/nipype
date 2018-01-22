# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import os

from ...base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine,
                     TraitedSpec, File, Directory, traits, isdefined,
                     InputMultiObject, OutputMultiObject)


class HistogramMatchingFilterInputSpec(CommandLineInputSpec):
    inputVolume = File(
        desc="The Input image to be computed for statistics",
        exists=True,
        argstr="--inputVolume %s")
    referenceVolume = File(
        desc="The Input image to be computed for statistics",
        exists=True,
        argstr="--referenceVolume %s")
    outputVolume = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Output Image File Name",
        argstr="--outputVolume %s")
    referenceBinaryVolume = File(
        desc="referenceBinaryVolume",
        exists=True,
        argstr="--referenceBinaryVolume %s")
    inputBinaryVolume = File(
        desc="inputBinaryVolume", exists=True, argstr="--inputBinaryVolume %s")
    numberOfMatchPoints = traits.Int(
        desc=" number of histogram matching points",
        argstr="--numberOfMatchPoints %d")
    numberOfHistogramBins = traits.Int(
        desc=" number of histogram bin", argstr="--numberOfHistogramBins %d")
    writeHistogram = traits.Str(
        desc=
        " decide if histogram data would be written with prefixe of the file name",
        argstr="--writeHistogram %s")
    histogramAlgorithm = traits.Enum(
        "OtsuHistogramMatching",
        desc=" histogram algrithm selection",
        argstr="--histogramAlgorithm %s")
    verbose = traits.Bool(
        desc=" verbose mode running for debbuging", argstr="--verbose ")


class HistogramMatchingFilterOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output Image File Name", exists=True)


class HistogramMatchingFilter(SEMLikeCommandLine):
    """title: Write Out Image Intensities

category: BRAINS.Utilities

description: For Analysis

version: 0.1

contributor: University of Iowa Department of Psychiatry, http:://www.psychiatry.uiowa.edu

"""

    input_spec = HistogramMatchingFilterInputSpec
    output_spec = HistogramMatchingFilterOutputSpec
    _cmd = " HistogramMatchingFilter "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}
    _redirect_x = False


class GenerateEdgeMapImageInputSpec(CommandLineInputSpec):
    inputMRVolumes = InputMultiObject(
        File(exists=True),
        desc=
        "List of input structural MR volumes to create the maximum edgemap",
        argstr="--inputMRVolumes %s...")
    inputMask = File(
        desc=
        "Input mask file name. If set, image histogram percentiles will be calculated within the mask",
        exists=True,
        argstr="--inputMask %s")
    minimumOutputRange = traits.Int(
        desc=
        "Map lower quantile and below to minimum output range. It should be a small number greater than zero. Default is 1",
        argstr="--minimumOutputRange %d")
    maximumOutputRange = traits.Int(
        desc=
        "Map upper quantile and above to maximum output range. Default is 255 that is the maximum range of unsigned char",
        argstr="--maximumOutputRange %d")
    lowerPercentileMatching = traits.Float(
        desc=
        "Map lower quantile and below to minOutputRange. It should be a value between zero and one",
        argstr="--lowerPercentileMatching %f")
    upperPercentileMatching = traits.Float(
        desc=
        "Map upper quantile and above to maxOutputRange. It should be a value between zero and one",
        argstr="--upperPercentileMatching %f")
    outputEdgeMap = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="output edgemap file name",
        argstr="--outputEdgeMap %s")
    outputMaximumGradientImage = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="output gradient image file name",
        argstr="--outputMaximumGradientImage %s")
    numberOfThreads = traits.Int(
        desc="Explicitly specify the maximum number of threads to use.",
        argstr="--numberOfThreads %d")


class GenerateEdgeMapImageOutputSpec(TraitedSpec):
    outputEdgeMap = File(desc="(required) output file name", exists=True)
    outputMaximumGradientImage = File(
        desc="output gradient image file name", exists=True)


class GenerateEdgeMapImage(SEMLikeCommandLine):
    """title: GenerateEdgeMapImage

category: BRAINS.Utilities

description: Automatic edgemap generation for edge-guided super-resolution reconstruction

version: 1.0

contributor: Ali Ghayoor

"""

    input_spec = GenerateEdgeMapImageInputSpec
    output_spec = GenerateEdgeMapImageOutputSpec
    _cmd = " GenerateEdgeMapImage "
    _outputs_filenames = {
        'outputEdgeMap': 'outputEdgeMap',
        'outputMaximumGradientImage': 'outputMaximumGradientImage'
    }
    _redirect_x = False


class GeneratePurePlugMaskInputSpec(CommandLineInputSpec):
    inputImageModalities = InputMultiObject(
        File(exists=True),
        desc="List of input image file names to create pure plugs mask",
        argstr="--inputImageModalities %s...")
    threshold = traits.Float(
        desc="threshold value to define class membership",
        argstr="--threshold %f")
    numberOfSubSamples = InputMultiObject(
        traits.Int,
        desc=
        "Number of continous index samples taken at each direction of lattice space for each plug volume",
        sep=",",
        argstr="--numberOfSubSamples %s")
    outputMaskFile = traits.Either(
        traits.Bool,
        File(),
        hash_files=False,
        desc="Output binary mask file name",
        argstr="--outputMaskFile %s")


class GeneratePurePlugMaskOutputSpec(TraitedSpec):
    outputMaskFile = File(
        desc="(required) Output binary mask file name", exists=True)


class GeneratePurePlugMask(SEMLikeCommandLine):
    """title: GeneratePurePlugMask

category: BRAINS.Utilities

description: This program gets several modality image files and returns a binary mask that defines the pure plugs

version: 1.0

contributor: Ali Ghayoor

"""

    input_spec = GeneratePurePlugMaskInputSpec
    output_spec = GeneratePurePlugMaskOutputSpec
    _cmd = " GeneratePurePlugMask "
    _outputs_filenames = {'outputMaskFile': 'outputMaskFile'}
    _redirect_x = False
