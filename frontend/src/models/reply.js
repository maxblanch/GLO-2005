const reply = {
  from: replyData => {
    return {
      comment: replyData.comment,
      date: replyData.date,
      managerId: replyData.manager_id,
      reviewId: replyData.review_id
    };
  }
};

export default reply;
