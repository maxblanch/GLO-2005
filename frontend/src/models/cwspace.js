const cwspace = {
  from: cwspaceData => {
    return {
      address: cwspaceData.address,
      city: cwspaceData.city,
      country: cwspaceData.country,
      currency: cwspaceData.currency,
      cwsId: cwspaceData.cws_id,
      dayPrice: cwspaceData.day_price,
      description: cwspaceData.description,
      imageUrl: cwspaceData.image_url,
      managerId: cwspaceData.manager_id,
      monthPrice: cwspaceData.month_price,
      name: cwspaceData.name,
      postalArea: cwspaceData.postal_area,
      rating: cwspaceData.rating,
      state: cwspaceData.state,
      weekPrice: cwspaceData.week_price,
      cityRoute: `/cities/${cwspaceData.city}`
    };
  }
};

export default cwspace;
