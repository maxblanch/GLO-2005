const review = {
  from: reviewData => {
    return {
      comment: reviewData.comment,
      coworkerId: reviewData.coworker_id,
      cwsId: reviewData.cws_id,
      date: reviewData.date,
      rating: reviewData.rating,
      reviewId: reviewData.review_id,
      title: reviewData.title
    };
  }
};

export default review;
