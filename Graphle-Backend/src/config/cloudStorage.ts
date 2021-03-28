/* eslint-disable camelcase */
import { Bucket, Storage } from '@google-cloud/storage';
import { client_email, GOOGLE_CLOUD_BUCKET, GOOGLE_CLOUD_PROJECT_ID, private_key } from './env';

const bucketName: string = GOOGLE_CLOUD_BUCKET;

const storage: Storage = new Storage({
	projectId: GOOGLE_CLOUD_PROJECT_ID,
	credentials: {
		client_email,
		private_key: private_key.replace(/\\n/g, '\n')
	}
});
const bucket: Bucket = storage.bucket(bucketName);

export { bucketName, storage, bucket };
