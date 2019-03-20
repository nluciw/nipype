# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""The fsl module provides classes for interfacing with the `FSL
<http://www.fmrib.ox.ac.uk/fsl/index.html>`_ command line tools.  This
was written to work with FSL version 6.0.1.
"""

from ..base import (TraitedSpec, File, traits)
from .base import (FSLCommand, FSLCommandInputSpec)

class ASLFileInputSpec(FSLCommandInputSpec):
    in_file = File(
        exists=True, 
        mandatory=True, 
        argstr='--data=%s',
        desc='the input brain-extracted asl series')
    out_file = File(
        desc='name of output difference image',
        argstr='--out=%s',
        genfile=True,
        hash_files=False)
    num_pld = traits.Int(
        desc='number of PLDs',
        argstr='--ntis=%d',
        mandatory=True)
    diff = traits.Bool(
        desc='Take the difference between pairs',
        argstr='--diff')
    input_form = traits.Enum(
        'diff',
        'tc',
        'ct',
        argstr='--iaf=%s',
        desc='ASL data form (differenced, tag-control, or control-tag)')
        
class ASLFileOutputSpec(TraitedSpec):
    out_file = File(desc='path/name of ASL difference images')
    
class ASLFile(FSLCommand):
    """FSL asl_file wrapper for ASL MRI manipulation.
    
    For complete details, see the asl_file docs.
    <https://asl-docs.readthedocs.io/en/latest/aslfile.html>
    """

    _cmd = 'asl_file'
    
    input_spec = ASLFileInputSpec
    
    output_spec = ASLFileOutputSpec
    
class BASILInputSpec(FSLCommandInputSpec):
    in_file = File(
        desc='Input containing differenced ASL data.',
        mandatory=True,
        argstr='-i %s',
        exists=True)
    out_basename = File(
        desc='Base name of output files.',
        mandatory=True,
        argstr='-o %s')
    mask = File(
        desc='Mask file.',
        exists=True,
        argstr='-m %s')
    parameters = File(
        desc='Model and sequence parameter file.',
        exists=True,
        argstr='-@ %s')
    spatial = traits.Bool(
        desc='Apply spatial regularising prior (instead of smoothing)',
        argstr='--spatial')
        
class BASIL(FSLCommand):
    """FSL BASIL wrapper for kinetic model inversion on ASL difference data.
    
    For complete detals, see the BASIL docs.
    <https://asl-docs.readthedocs.io/en/latest/basilcmd.html>
    """
    
    _cmd = 'basil'
    
    input_spec = BASILInputSpec