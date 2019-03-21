# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""The fsl module provides classes for interfacing with the `FSL
<http://www.fmrib.ox.ac.uk/fsl/index.html>`_ command line tools.  This
was written to work with FSL version 6.0.1.
"""
import os

from ..base import (TraitedSpec, File, traits, isdefined)
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
    difference_type = traits.Enum(
        '--diff',
        '--surrdiff',
        desc='Do pairwise subtraction, using conventional (producing N/2 volumes) or surround subtraction (producing N-1).',
        argstr='%s')
    input_form = traits.Enum(
        'diff',
        'tc',
        'ct',
        argstr='--iaf=%s',
        desc='ASL data form (differenced, tag-control, or control-tag)')
    block_format = traits.Enum(
        'tis',
        'rpt',
        argstr='--ibf=%s',
        desc='Multi-PLD block format (same PLD grouped together [T1 T1 T2 T2 T3 T3], or PLD sets [T1 T2 T3 T1 T2 T3])')
        
class ASLFileOutputSpec(TraitedSpec):
    asl_difference_file = File(
        exists=True, desc='ASL difference images')

class ASLFile(FSLCommand):
    """FSL asl_file wrapper for ASL MRI manipulation.
    
    For complete details, see the asl_file docs.
    <https://asl-docs.readthedocs.io/en/latest/aslfile.html>
    """

    _cmd = 'asl_file'
    
    input_spec = ASLFileInputSpec
    output_spec = ASLFileOutputSpec

    def _list_outputs(self):
        outputs = self._outputs().get()
        out_file = self.inputs.out_file
        if not isdefined(out_file):
            out_file = self._gen_fname(self.inputs.in_file, suffix='_diff')
        outputs['asl_difference_file'] = os.path.abspath(out_file)
        return outputs

    def _gen_filename(self, name):
        if name == 'out_file':
            return self._list_outputs()['asl_difference_file']
        return None
    
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
    inferart = traits.Bool(
        desc='Add macrovascular component to the model',
        argstr='--inferart')
        
class BASIL(FSLCommand):
    """FSL BASIL wrapper for kinetic model inversion on ASL difference data.
    
    For complete detals, see the BASIL docs.
    <https://asl-docs.readthedocs.io/en/latest/basilcmd.html>
    """
    
    _cmd = 'basil'
    
    input_spec = BASILInputSpec