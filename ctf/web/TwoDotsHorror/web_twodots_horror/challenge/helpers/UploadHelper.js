const fs         = require('fs');
const path       = require('path');
const isJpg      = require('is-jpg');
const sizeOf     = require('image-size');

module.exports = {
	async uploadImage(file) {
		return new Promise(async (resolve, reject) => {
			if(file == undefined) return reject(new Error("Please select a file to upload!"));
			try{
				if (!isJpg(file.data)) return reject(new Error("Please upload a valid JPEG image!"));
				const dimensions = sizeOf(file.data);
				if(!(dimensions.width >= 120 && dimensions.height >= 120)) {
					return reject(new Error("Image size must be at least 120x120!"));
				}
				uploadPath = path.join(__dirname, '/../uploads', file.md5);
				file.mv(uploadPath, (err) => {
					if (err) return reject(err);
				});
				return resolve(file.md5);
			}catch (e){
				console.log(e);
				reject(e);
			}
			
		});
	}
}