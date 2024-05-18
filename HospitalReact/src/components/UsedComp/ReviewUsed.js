import React from 'react';
import { ReviewTable } from '../Tables';
import { reviewData } from '../Datas';

function ReviewsUsed() {
  return (
    <div className="w-full">
      <h1 className="text-sm font-medium mb-6">Reviews</h1>
      <div className="w-full overflow-x-scroll">
        <ReviewTable doctor={true} data={reviewData.slice(0, 3)} />
      </div>
    </div>
  );
}

export default ReviewsUsed;
