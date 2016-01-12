# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class MultiplyScalarVolumesInputSpec(CommandLineInputSpec):
    inputVolume1 = File(position=-3, desc="Input volume 1", exists=True, argstr="%s")
    inputVolume2 = File(position=-2, desc="Input volume 2", exists=True, argstr="%s")
    outputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Volume1 * Volume2", argstr="%s")
    order = traits.Enum("0", "1", "2", "3", desc="Interpolation order if two images are in different coordinate frames or have different sampling.", argstr="--order %s")


class MultiplyScalarVolumesOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Volume1 * Volume2", exists=True)


class MultiplyScalarVolumes(SEMLikeCommandLine):
    """title: Multiply Scalar Volumes

category: Filtering.Arithmetic

description: Multiplies two images. Although all image types are supported on input, only signed types are produced. The two images do not have to have the same dimensions.

version: 0.1.0.$Revision: 8595 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/Multiply

contributor: Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = MultiplyScalarVolumesInputSpec
    output_spec = MultiplyScalarVolumesOutputSpec
    _cmd = "MultiplyScalarVolumes "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class MaskScalarVolumeInputSpec(CommandLineInputSpec):
    InputVolume = File(position=-3, desc="Input volume to be masked", exists=True, argstr="%s")
    MaskVolume = File(position=-2, desc="Label volume containing the mask", exists=True, argstr="%s")
    OutputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Output volume: Input Volume masked by label value from Mask Volume", argstr="%s")
    label = traits.Int(desc="Label value in the Mask Volume to use as the mask", argstr="--label %d")
    replace = traits.Int(desc="Value to use for the output volume outside of the mask", argstr="--replace %d")


class MaskScalarVolumeOutputSpec(TraitedSpec):
    OutputVolume = File(position=-1, desc="Output volume: Input Volume masked by label value from Mask Volume", exists=True)


class MaskScalarVolume(SEMLikeCommandLine):
    """title: Mask Scalar Volume

category: Filtering.Arithmetic

description: Masks two images. The output image is set to 0 everywhere except where the chosen label from the mask volume is present, at which point it will retain it's original values. Although all image types are supported on input, only signed types are produced. The two images do not have to have the same dimensions.

version: 0.1.0.$Revision: 8595 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/Mask

contributor: Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = MaskScalarVolumeInputSpec
    output_spec = MaskScalarVolumeOutputSpec
    _cmd = "MaskScalarVolume "
    _outputs_filenames = {'OutputVolume': 'OutputVolume.nii'}


class SubtractScalarVolumesInputSpec(CommandLineInputSpec):
    inputVolume1 = File(position=-3, desc="Input volume 1", exists=True, argstr="%s")
    inputVolume2 = File(position=-2, desc="Input volume 2", exists=True, argstr="%s")
    outputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Volume1 - Volume2", argstr="%s")
    order = traits.Enum("0", "1", "2", "3", desc="Interpolation order if two images are in different coordinate frames or have different sampling.", argstr="--order %s")


class SubtractScalarVolumesOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Volume1 - Volume2", exists=True)


class SubtractScalarVolumes(SEMLikeCommandLine):
    """title: Subtract Scalar Volumes

category: Filtering.Arithmetic

description: Subtracts two images. Although all image types are supported on input, only signed types are produced. The two images do not have to have the same dimensions.

version: 0.1.0.$Revision: 19608 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/Subtract

contributor: Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = SubtractScalarVolumesInputSpec
    output_spec = SubtractScalarVolumesOutputSpec
    _cmd = "SubtractScalarVolumes "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class AddScalarVolumesInputSpec(CommandLineInputSpec):
    inputVolume1 = File(position=-3, desc="Input volume 1", exists=True, argstr="%s")
    inputVolume2 = File(position=-2, desc="Input volume 2", exists=True, argstr="%s")
    outputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Volume1 + Volume2", argstr="%s")
    order = traits.Enum("0", "1", "2", "3", desc="Interpolation order if two images are in different coordinate frames or have different sampling.", argstr="--order %s")


class AddScalarVolumesOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Volume1 + Volume2", exists=True)


class AddScalarVolumes(SEMLikeCommandLine):
    """title: Add Scalar Volumes

category: Filtering.Arithmetic

description: Adds two images. Although all image types are supported on input, only signed types are produced. The two images do not have to have the same dimensions.

version: 0.1.0.$Revision: 19608 $(alpha)

documentation-url: http://slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/Add

contributor: Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = AddScalarVolumesInputSpec
    output_spec = AddScalarVolumesOutputSpec
    _cmd = "AddScalarVolumes "
    _outputs_filenames = {'outputVolume': 'outputVolume.nii'}


class CastScalarVolumeInputSpec(CommandLineInputSpec):
    InputVolume = File(position=-2, desc="Input volume, the volume to cast.", exists=True, argstr="%s")
    OutputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Output volume, cast to the new type.", argstr="%s")
    type = traits.Enum("Char", "UnsignedChar", "Short", "UnsignedShort", "Int", "UnsignedInt", "Float", "Double", desc="Type for the new output volume.", argstr="--type %s")


class CastScalarVolumeOutputSpec(TraitedSpec):
    OutputVolume = File(position=-1, desc="Output volume, cast to the new type.", exists=True)


class CastScalarVolume(SEMLikeCommandLine):
    """title: Cast Scalar Volume

category: Filtering.Arithmetic

description: Cast a volume to a given data type.
Use at your own risk when casting an input volume into a lower precision type!
Allows casting to the same type as the input volume.

version: 0.1.0.$Revision: 2104 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/Cast

contributor: Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = CastScalarVolumeInputSpec
    output_spec = CastScalarVolumeOutputSpec
    _cmd = "CastScalarVolume "
    _outputs_filenames = {'OutputVolume': 'OutputVolume.nii'}
