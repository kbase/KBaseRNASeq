# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport
import time


class KBaseRNASeq(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver=None,
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('KBaseRNASeq', job_id)

    def _CreateRNASeqSampleSet_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.CreateRNASeqSampleSet', [params],
             self._service_ver, context)

    def CreateRNASeqSampleSet(self, params, context=None):
        """
        :param params: instance of type "CreateRNASeqSampleSetParams"
           (FUNCTIONS used in the service) -> structure: parameter "ws_id" of
           String, parameter "sampleset_id" of String, parameter
           "sampleset_desc" of String, parameter "domain" of String,
           parameter "platform" of String, parameter "sample_ids" of list of
           String, parameter "condition" of list of String, parameter
           "source" of String, parameter "Library_type" of String, parameter
           "publication_id" of String, parameter "external_source_date" of
           String
        :returns: instance of type "RNASeqSampleSet" (Object to Describe the
           RNASeq SampleSet @optional platform num_replicates source
           publication_Id external_source_date sample_ids @metadata ws
           sampleset_id @metadata ws platform @metadata ws num_samples
           @metadata ws num_replicates @metadata ws length(condition)) ->
           structure: parameter "sampleset_id" of String, parameter
           "sampleset_desc" of String, parameter "domain" of String,
           parameter "platform" of String, parameter "num_samples" of Long,
           parameter "num_replicates" of Long, parameter "sample_ids" of list
           of String, parameter "condition" of list of String, parameter
           "source" of String, parameter "Library_type" of String, parameter
           "publication_Id" of String, parameter "external_source_date" of
           String
        """
        job_id = self._CreateRNASeqSampleSet_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _BuildBowtie2Index_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.BuildBowtie2Index', [params],
             self._service_ver, context)

    def BuildBowtie2Index(self, params, context=None):
        """
        :param params: instance of type "Bowtie2IndexParams" -> structure:
           parameter "ws_id" of String, parameter "reference" of String,
           parameter "output_obj_name" of String
        :returns: instance of type "ResultsToReport" (Object for Report type)
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        job_id = self._BuildBowtie2Index_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _Bowtie2Call_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.Bowtie2Call', [params],
             self._service_ver, context)

    def Bowtie2Call(self, params, context=None):
        """
        :param params: instance of type "Bowtie2Params" -> structure:
           parameter "ws_id" of String, parameter "sampleset_id" of String,
           parameter "genome_id" of String, parameter "bowtie_index" of
           String, parameter "phred33" of String, parameter "phred64" of
           String, parameter "local" of String, parameter "very-fast" of
           String, parameter "fast" of String, parameter "very-sensitive" of
           String, parameter "sensitive" of String, parameter
           "very-fast-local" of String, parameter "very-sensitive-local" of
           String, parameter "fast-local" of String, parameter
           "fast-sensitive" of String
        :returns: instance of type "ResultsToReport" (Object for Report type)
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        job_id = self._Bowtie2Call_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _Hisat2Call_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.Hisat2Call', [params],
             self._service_ver, context)

    def Hisat2Call(self, params, context=None):
        """
        :param params: instance of type "Hisat2Params" (****************) ->
           structure: parameter "ws_id" of String, parameter "sampleset_id"
           of String, parameter "genome_id" of String, parameter
           "num_threads" of Long, parameter "quality_score" of String,
           parameter "skip" of Long, parameter "trim3" of Long, parameter
           "trim5" of Long, parameter "np" of Long, parameter "minins" of
           Long, parameter "maxins" of Long, parameter "orientation" of
           String, parameter "min_intron_length" of Long, parameter
           "max_intron_length" of Long, parameter "no_spliced_alignment" of
           type "bool" (indicates true or false values, false <= 0, true
           >=1), parameter "transcriptome_mapping_only" of type "bool"
           (indicates true or false values, false <= 0, true >=1), parameter
           "tailor_alignments" of String
        :returns: instance of type "ResultsToReport" (Object for Report type)
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        job_id = self._Hisat2Call_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def Hisat2Call_prepare(self, prepare_params, context=None):
        """
        :param prepare_params: instance of type
           "Hisat2Call_prepareInputParams" -> structure: parameter
           "global_input_params" of type "Hisat2Call_globalInputParams"
           (***************************) -> structure: parameter "ws_id" of
           String, parameter "read_sample" of String, parameter "genome_id"
           of String, parameter "read_mismatches" of Long, parameter
           "read_gap_length" of Long, parameter "read_edit_dist" of Long,
           parameter "min_intron_length" of Long, parameter
           "max_intron_length" of Long, parameter "num_threads" of Long,
           parameter "report_secondary_alignments" of String, parameter
           "no_coverage_search" of String, parameter "library_type" of
           String, parameter "annotation_gtf" of type
           "ws_referenceAnnotation_id" (Id for KBaseRNASeq.GFFAnnotation @id
           ws KBaseRNASeq.GFFAnnotation), parameter "user_token" of String
        :returns: instance of type "Hisat2Call_prepareSchedule" -> structure:
           parameter "tasks" of list of type "Hisat2Call_runEachInput" ->
           structure: parameter "input_arguments" of tuple of size 1: type
           "Hisat2Call_task" -> structure: parameter "job_id" of String,
           parameter "label" of String, parameter "hisat2_dir" of String,
           parameter "ws_id" of String, parameter "reads_type" of String,
           parameter "annotation_id" of String, parameter "sampleset_id" of
           String, parameter "gtf_file" of String, parameter "bowtie_index"
           of String
        """
        return self._client.call_method(
            'KBaseRNASeq.Hisat2Call_prepare',
            [prepare_params], self._service_ver, context)

    def _Hisat2Call_runEach_submit(self, task, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.Hisat2Call_runEach', [task],
             self._service_ver, context)

    def Hisat2Call_runEach(self, task, context=None):
        """
        :param task: instance of type "Hisat2Call_task" -> structure:
           parameter "job_id" of String, parameter "label" of String,
           parameter "hisat2_dir" of String, parameter "ws_id" of String,
           parameter "reads_type" of String, parameter "annotation_id" of
           String, parameter "sampleset_id" of String, parameter "gtf_file"
           of String, parameter "bowtie_index" of String
        :returns: instance of type "Hisat2Call_runEachResult"
           (*****************************) -> structure: parameter
           "read_sample" of String, parameter "output_name" of String
        """
        job_id = self._Hisat2Call_runEach_submit(task, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def Hisat2Call_collect(self, collect_params, context=None):
        """
        :param collect_params: instance of type
           "Hisat2Call_collectInputParams" -> structure: parameter
           "global_params" of type "Hisat2Call_globalInputParams"
           (***************************) -> structure: parameter "ws_id" of
           String, parameter "read_sample" of String, parameter "genome_id"
           of String, parameter "read_mismatches" of Long, parameter
           "read_gap_length" of Long, parameter "read_edit_dist" of Long,
           parameter "min_intron_length" of Long, parameter
           "max_intron_length" of Long, parameter "num_threads" of Long,
           parameter "report_secondary_alignments" of String, parameter
           "no_coverage_search" of String, parameter "library_type" of
           String, parameter "annotation_gtf" of type
           "ws_referenceAnnotation_id" (Id for KBaseRNASeq.GFFAnnotation @id
           ws KBaseRNASeq.GFFAnnotation), parameter "user_token" of String,
           parameter "input_result_pairs" of list of type
           "Hisat2Call_InputResultPair" (*****************************) ->
           structure: parameter "input" of type "Hisat2Call_runEachInput" ->
           structure: parameter "input_arguments" of tuple of size 1: type
           "Hisat2Call_task" -> structure: parameter "job_id" of String,
           parameter "label" of String, parameter "hisat2_dir" of String,
           parameter "ws_id" of String, parameter "reads_type" of String,
           parameter "annotation_id" of String, parameter "sampleset_id" of
           String, parameter "gtf_file" of String, parameter "bowtie_index"
           of String, parameter "result" of type "Hisat2Call_runEachResult"
           (*****************************) -> structure: parameter
           "read_sample" of String, parameter "output_name" of String
        :returns: instance of type "Hisat2Call_globalResult" -> structure:
           parameter "output" of String, parameter "jobs" of list of tuple of
           size 2: parameter "job_number" of Long, parameter "message" of
           String
        """
        return self._client.call_method(
            'KBaseRNASeq.Hisat2Call_collect',
            [collect_params], self._service_ver, context)

    def _TophatCall_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.TophatCall', [params],
             self._service_ver, context)

    def TophatCall(self, params, context=None):
        """
        :param params: instance of type "TophatCall_globalInputParams"
           (****************) -> structure: parameter "ws_id" of String,
           parameter "sampleset_id" of String, parameter "genome_id" of
           String, parameter "bowtie2_index" of String, parameter
           "read_mismatches" of Long, parameter "read_gap_length" of Long,
           parameter "read_edit_dist" of Long, parameter "min_intron_length"
           of Long, parameter "max_intron_length" of Long, parameter
           "num_threads" of Long, parameter "report_secondary_alignments" of
           String, parameter "no_coverage_search" of String, parameter
           "library_type" of String, parameter "annotation_gtf" of type
           "ws_referenceAnnotation_id" (Id for KBaseRNASeq.GFFAnnotation @id
           ws KBaseRNASeq.GFFAnnotation), parameter "is_sample_set" of Long
        :returns: instance of type "ResultsToReport" (Object for Report type)
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        job_id = self._TophatCall_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def TophatCall_prepare(self, prepare_params, context=None):
        """
        :param prepare_params: instance of type
           "TophatCall_prepareInputParams" (***************************) ->
           structure: parameter "global_input_params" of type
           "TophatCall_globalInputParams" (****************) -> structure:
           parameter "ws_id" of String, parameter "sampleset_id" of String,
           parameter "genome_id" of String, parameter "bowtie2_index" of
           String, parameter "read_mismatches" of Long, parameter
           "read_gap_length" of Long, parameter "read_edit_dist" of Long,
           parameter "min_intron_length" of Long, parameter
           "max_intron_length" of Long, parameter "num_threads" of Long,
           parameter "report_secondary_alignments" of String, parameter
           "no_coverage_search" of String, parameter "library_type" of
           String, parameter "annotation_gtf" of type
           "ws_referenceAnnotation_id" (Id for KBaseRNASeq.GFFAnnotation @id
           ws KBaseRNASeq.GFFAnnotation), parameter "is_sample_set" of Long
        :returns: instance of type "TophatCall_prepareSchedule" -> structure:
           parameter "tasks" of list of type "TophatCall_runEachInput" ->
           structure: parameter "input_arguments" of tuple of size 1: type
           "TophatCall_task" -> structure: parameter "job_id" of String,
           parameter "label" of String, parameter "tophat_dir" of String,
           parameter "ws_id" of String, parameter "reads_type" of String,
           parameter "annotation_id" of String, parameter "sampleset_id" of
           String, parameter "gtf_file" of String, parameter "bowtie_index"
           of String
        """
        return self._client.call_method(
            'KBaseRNASeq.TophatCall_prepare',
            [prepare_params], self._service_ver, context)

    def _TophatCall_runEach_submit(self, task, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.TophatCall_runEach', [task],
             self._service_ver, context)

    def TophatCall_runEach(self, task, context=None):
        """
        :param task: instance of type "TophatCall_task" -> structure:
           parameter "job_id" of String, parameter "label" of String,
           parameter "tophat_dir" of String, parameter "ws_id" of String,
           parameter "reads_type" of String, parameter "annotation_id" of
           String, parameter "sampleset_id" of String, parameter "gtf_file"
           of String, parameter "bowtie_index" of String
        :returns: instance of type "TophatCall_runEachResult"
           (*****************************) -> structure: parameter
           "sample_set_id" of String, parameter "output_name" of String
        """
        job_id = self._TophatCall_runEach_submit(task, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def TophatCall_collect(self, collect_params, context=None):
        """
        :param collect_params: instance of type
           "TophatCall_collectInputParams" -> structure: parameter
           "global_params" of type "TophatCall_globalInputParams"
           (****************) -> structure: parameter "ws_id" of String,
           parameter "sampleset_id" of String, parameter "genome_id" of
           String, parameter "bowtie2_index" of String, parameter
           "read_mismatches" of Long, parameter "read_gap_length" of Long,
           parameter "read_edit_dist" of Long, parameter "min_intron_length"
           of Long, parameter "max_intron_length" of Long, parameter
           "num_threads" of Long, parameter "report_secondary_alignments" of
           String, parameter "no_coverage_search" of String, parameter
           "library_type" of String, parameter "annotation_gtf" of type
           "ws_referenceAnnotation_id" (Id for KBaseRNASeq.GFFAnnotation @id
           ws KBaseRNASeq.GFFAnnotation), parameter "is_sample_set" of Long,
           parameter "input_result_pairs" of list of type
           "TophatCall_InputResultPair" (*****************************) ->
           structure: parameter "input" of type "TophatCall_runEachInput" ->
           structure: parameter "input_arguments" of tuple of size 1: type
           "TophatCall_task" -> structure: parameter "job_id" of String,
           parameter "label" of String, parameter "tophat_dir" of String,
           parameter "ws_id" of String, parameter "reads_type" of String,
           parameter "annotation_id" of String, parameter "sampleset_id" of
           String, parameter "gtf_file" of String, parameter "bowtie_index"
           of String, parameter "result" of type "TophatCall_runEachResult"
           (*****************************) -> structure: parameter
           "sample_set_id" of String, parameter "output_name" of String
        :returns: instance of type "TophatCall_globalResult" -> structure:
           parameter "output" of unspecified object, parameter "workspace" of
           String
        """
        return self._client.call_method(
            'KBaseRNASeq.TophatCall_collect',
            [collect_params], self._service_ver, context)

    def _StringTieCall_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.StringTieCall', [params],
             self._service_ver, context)

    def StringTieCall(self, params, context=None):
        """
        :param params: instance of type "StringTieParams" -> structure:
           parameter "ws_id" of String, parameter "sample_alignment" of
           String, parameter "num-threads" of Long, parameter "label" of
           String, parameter "min_isoform_abundance" of Double, parameter
           "a_juncs" of Long, parameter "min_length" of Long, parameter
           "j_min_reads" of Double, parameter "c_min_read_coverage" of
           Double, parameter "gap_sep_value" of Long, parameter
           "disable_trimming" of type "bool" (indicates true or false values,
           false <= 0, true >=1), parameter "ballgown_mode" of type "bool"
           (indicates true or false values, false <= 0, true >=1), parameter
           "skip_reads_with_no_ref" of type "bool" (indicates true or false
           values, false <= 0, true >=1), parameter "merge" of String
        :returns: instance of type "ResultsToReport" (Object for Report type)
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        job_id = self._StringTieCall_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _CufflinksCall_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.CufflinksCall', [params],
             self._service_ver, context)

    def CufflinksCall(self, params, context=None):
        """
        :param params: instance of type "CufflinksCall_runParams" ->
           structure: parameter "global_input_params" of type
           "CufflinksCall_globalInputParams" (*******************) ->
           structure: parameter "ws_id" of String, parameter
           "sample_alignment" of String, parameter "num_threads" of Long,
           parameter "min-intron-length" of Long, parameter
           "max-intron-length" of Long, parameter "overhang-tolerance" of Long
        :returns: instance of type "ResultsToReport" (Object for Report type)
           -> structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        job_id = self._CufflinksCall_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def CufflinksCall_prepare(self, prepare_params, context=None):
        """
        :param prepare_params: instance of type
           "CufflinksCall_prepareInputParams" (**************************) ->
           structure: parameter "global_input_params" of type
           "CufflinksCall_globalInputParams" (*******************) ->
           structure: parameter "ws_id" of String, parameter
           "sample_alignment" of String, parameter "num_threads" of Long,
           parameter "min-intron-length" of Long, parameter
           "max-intron-length" of Long, parameter "overhang-tolerance" of Long
        :returns: instance of type "CufflinksCall_prepareSchedule" ->
           structure: parameter "tasks" of list of type
           "CufflinksCall_runEachInput" -> structure: parameter
           "input_arguments" of tuple of size 1: type "CufflinksCall_task" ->
           structure:
        """
        return self._client.call_method(
            'KBaseRNASeq.CufflinksCall_prepare',
            [prepare_params], self._service_ver, context)

    def _CufflinksCall_runEach_submit(self, task, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.CufflinksCall_runEach', [task],
             self._service_ver, context)

    def CufflinksCall_runEach(self, task, context=None):
        """
        :param task: instance of type "CufflinksCall_task" -> structure:
        :returns: instance of type "CufflinksCall_runEachResult"
           (**************************) -> structure: parameter
           "alignment_set_id" of String, parameter "output_name" of String
        """
        job_id = self._CufflinksCall_runEach_submit(task, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def CufflinksCall_collect(self, collect_params, context=None):
        """
        :param collect_params: instance of type
           "CufflinksCall_collectInputParams" -> structure: parameter
           "global_params" of type "CufflinksCall_globalInputParams"
           (*******************) -> structure: parameter "ws_id" of String,
           parameter "sample_alignment" of String, parameter "num_threads" of
           Long, parameter "min-intron-length" of Long, parameter
           "max-intron-length" of Long, parameter "overhang-tolerance" of
           Long, parameter "input_result_pairs" of list of type
           "CufflinksCall_InputResultPair" (**************************) ->
           structure: parameter "input" of type "CufflinksCall_runEachInput"
           -> structure: parameter "input_arguments" of tuple of size 1: type
           "CufflinksCall_task" -> structure: , parameter "result" of type
           "CufflinksCall_runEachResult" (**************************) ->
           structure: parameter "alignment_set_id" of String, parameter
           "output_name" of String
        :returns: instance of type "CufflinksCall_globalResult" -> structure:
           parameter "output" of unspecified object, parameter "workspace" of
           String
        """
        return self._client.call_method(
            'KBaseRNASeq.CufflinksCall_collect',
            [collect_params], self._service_ver, context)

    def _CuffdiffCall_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.CuffdiffCall', [params],
             self._service_ver, context)

    def CuffdiffCall(self, params, context=None):
        """
        :param params: instance of type "CuffdiffParams" -> structure:
           parameter "ws_id" of String, parameter "rnaseq_exp_details" of
           type "RNASeqSampleSet" (Object to Describe the RNASeq SampleSet
           @optional platform num_replicates source publication_Id
           external_source_date sample_ids @metadata ws sampleset_id
           @metadata ws platform @metadata ws num_samples @metadata ws
           num_replicates @metadata ws length(condition)) -> structure:
           parameter "sampleset_id" of String, parameter "sampleset_desc" of
           String, parameter "domain" of String, parameter "platform" of
           String, parameter "num_samples" of Long, parameter
           "num_replicates" of Long, parameter "sample_ids" of list of
           String, parameter "condition" of list of String, parameter
           "source" of String, parameter "Library_type" of String, parameter
           "publication_Id" of String, parameter "external_source_date" of
           String, parameter "output_obj_name" of String, parameter
           "time-series" of String, parameter "library-type" of String,
           parameter "library-norm-method" of String, parameter
           "multi-read-correct" of String, parameter "min-alignment-count" of
           Long, parameter "dispersion-method" of String, parameter
           "no-js-tests" of String, parameter "frag-len-mean" of Long,
           parameter "frag-len-std-dev" of Long, parameter
           "max-mle-iterations" of Long, parameter "compatible-hits-norm" of
           String, parameter "no-length-correction" of String
        :returns: instance of type "RNASeqDifferentialExpression" (Object
           RNASeqDifferentialExpression file structure @optional tool_opts
           tool_version sample_ids comments) -> structure: parameter
           "tool_used" of String, parameter "tool_version" of String,
           parameter "tool_opts" of list of mapping from String to String,
           parameter "file" of type "Handle" (@optional hid file_name type
           url remote_md5 remote_sha1) -> structure: parameter "hid" of type
           "HandleId" (Id for the handle object @id handle), parameter
           "file_name" of String, parameter "id" of String, parameter "type"
           of String, parameter "url" of String, parameter "remote_md5" of
           String, parameter "remote_sha1" of String, parameter "sample_ids"
           of list of String, parameter "condition" of list of String,
           parameter "genome_id" of String, parameter "expressionSet_id" of
           type "ws_expressionSet_id" (Id for expression sample set @id ws
           KBaseRNASeq.RNASeqExpressionSet), parameter "alignmentSet_id" of
           type "ws_alignmentSet_id" (The workspace id for a
           RNASeqAlignmentSet object @id ws KBaseRNASeq.RNASeqAlignmentSet),
           parameter "sampleset_id" of type "ws_Sampleset_id" (Id for
           KBaseRNASeq.RNASeqSampleSet @id ws KBaseRNASeq.RNASeqSampleSet),
           parameter "comments" of String
        """
        job_id = self._CuffdiffCall_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _DiffExpCallforBallgown_submit(self, params, context=None):
        return self._client._submit_job(
             'KBaseRNASeq.DiffExpCallforBallgown', [params],
             self._service_ver, context)

    def DiffExpCallforBallgown(self, params, context=None):
        """
        :param params: instance of type "DifferentialExpParams" -> structure:
           parameter "ws_id" of String, parameter "expressionset_id" of type
           "RNASeqExpressionSet" (Set object for RNASeqExpression objects
           @optional sample_ids condition tool_used tool_version tool_opts
           @metadata ws tool_used @metadata ws tool_version @metadata ws
           alignmentSet_id) -> structure: parameter "tool_used" of String,
           parameter "tool_version" of String, parameter "tool_opts" of
           mapping from String to String, parameter "alignmentSet_id" of type
           "ws_alignmentSet_id" (The workspace id for a RNASeqAlignmentSet
           object @id ws KBaseRNASeq.RNASeqAlignmentSet), parameter
           "sampleset_id" of type "ws_Sampleset_id" (Id for
           KBaseRNASeq.RNASeqSampleSet @id ws KBaseRNASeq.RNASeqSampleSet),
           parameter "genome_id" of String, parameter "sample_ids" of list of
           String, parameter "condition" of list of String, parameter
           "sample_expression_ids" of list of type "ws_expression_sample_id"
           (Id for expression sample @id ws KBaseRNASeq.RNASeqExpression),
           parameter "mapped_expression_objects" of list of mapping from
           String to String, parameter "mapped_expression_ids" of list of
           mapping from String to type "ws_expression_sample_id" (Id for
           expression sample @id ws KBaseRNASeq.RNASeqExpression), parameter
           "output_obj_name" of String, parameter "num_threads" of Long
        :returns: instance of type "RNASeqDifferentialExpression" (Object
           RNASeqDifferentialExpression file structure @optional tool_opts
           tool_version sample_ids comments) -> structure: parameter
           "tool_used" of String, parameter "tool_version" of String,
           parameter "tool_opts" of list of mapping from String to String,
           parameter "file" of type "Handle" (@optional hid file_name type
           url remote_md5 remote_sha1) -> structure: parameter "hid" of type
           "HandleId" (Id for the handle object @id handle), parameter
           "file_name" of String, parameter "id" of String, parameter "type"
           of String, parameter "url" of String, parameter "remote_md5" of
           String, parameter "remote_sha1" of String, parameter "sample_ids"
           of list of String, parameter "condition" of list of String,
           parameter "genome_id" of String, parameter "expressionSet_id" of
           type "ws_expressionSet_id" (Id for expression sample set @id ws
           KBaseRNASeq.RNASeqExpressionSet), parameter "alignmentSet_id" of
           type "ws_alignmentSet_id" (The workspace id for a
           RNASeqAlignmentSet object @id ws KBaseRNASeq.RNASeqAlignmentSet),
           parameter "sampleset_id" of type "ws_Sampleset_id" (Id for
           KBaseRNASeq.RNASeqSampleSet @id ws KBaseRNASeq.RNASeqSampleSet),
           parameter "comments" of String
        """
        job_id = self._DiffExpCallforBallgown_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def status(self, context=None):
        return self._client.call_method('KBaseRNASeq.status',
                                        [], self._service_ver, context)
