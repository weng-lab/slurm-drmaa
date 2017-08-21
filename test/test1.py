#!/usr/bin/env python

import drmaa
import os

def main():
	"""
	Submit a job.
	Note, need file called sleeper.sh in current directory.
	"""
	with drmaa.Session() as s:
		print('Creating job template')
		jt = s.createJobTemplate()
		#jt.remoteCommand = os.path.join(os.getcwd(), 'slurm.sh')
		jt.remoteCommand = "/usr/bin/env | grep SLURM"
		jt.workingDirectory = drmaa.JobTemplate.HOME_DIRECTORY
		#jt.outputPath =":"+drmaa.JobTemplate.HOME_DIRECTORY+'/DRMAA_JOB_OUT'
		#jt.args = ['a', 'b']
		#jt.joinFiles=True
		jt.joinFiles=False
		#jt.nativeSpecification = "--mincpus=1 --ntasks=0 --mem-per-cpu=10 --partition=zlurm"
		# not specifiying resources will make it take a full host per job

		jobid = 0
		#jobid = s.runJob(jt)
		jobid = s.runBulkJobs(jt, 1, 31, 1)


		print('Your job has been submitted with ID %s' % jobid)

		print('Cleaning up')
		s.deleteJobTemplate(jt)

if __name__=='__main__':
   main()

