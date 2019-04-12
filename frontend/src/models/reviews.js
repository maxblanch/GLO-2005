import review from "./review";

const reviews = {
  from: reviewsData => reviewsData.map(reviewData => review.from(reviewData))
};

export default reviews;
