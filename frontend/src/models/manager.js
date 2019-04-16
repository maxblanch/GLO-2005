const manager = {
  from: managerData => {
    return {
      address: managerData.address,
      city: managerData.city,
      country: managerData.country,
      email: managerData.email,
      firstName: managerData.first_name,
      gender: managerData.gender,
      lastName: managerData.last_name,
      managerId: managerData.manager_id,
      postalArea: managerData.postal_area,
      state: managerData.state,
      username: managerData.username
    };
  }
};

export default manager;
