import numpy as np


def compute_features(imdb, args):
    if args.feature == 'tinyimage':
        return tinyimage_features(imdb, args.tinyimage_patchdim)
    elif args.feature == 'bow-patches':
        return bow_patch_features(
            imdb, args.patches_dictionarysize, args.patches_radius,
            args.patches_stride)
    elif args.feature == 'bow-sift':
        return bow_sift_features(
            imdb, args.sift_dictionarysize, args.sift_radius,
            args.sift_stride)
    else:
        raise NotImplementedError('Selected feature not yet implemented')


def tinyimage_features(imdb, patchdim):
    '''
     Compute grayscale features by resizing the images into a patchdim x patchdim
     patch and resizing the image into a vector.
    '''
    raise NotImplementedError() # you should implement this


def bow_patch_features(imdb, dictionarysize, radius, stride):
    '''
     STEP 1: Write a function that extracts dense grayscale patches from an image
     STEP 2: Learn a dictionary
               -- sample many desriptors (~10k) from train+val images
               -- learn a dictionary using k-means
     STEP 3: Loop over all the images  and extract
             features (same as step 1). Build global histograms over these.
    '''

    raise NotImplementedError() # you should implement this


def bow_sift_features(imdb, dictionarysize, radius, stride):
    '''
    STEP 1: Write a function that extracts dense SIFT features from an image
    STEP 2: Learn a dictionary
               -- sample many desriptors (~10k) from train+val images
               -- learn a dictionary using k-means
     STEP 3: Loop over all the images  and compute
             features (same as step 1)

    '''
    raise NotImplementedError() # you should implement this
