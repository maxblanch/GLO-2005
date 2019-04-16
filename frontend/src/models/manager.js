const manager = {
  from: managerData => {
    return {
      address: managerData.address,
      city: managerData.city,
      country: managerData.country,
      email: managerData.email,
      firstName: managerData.firstName,
      gender: managerData.gender,
      lastName: managerData.lastName,
      managerId: managerData.manager_id,
      postalArea: managerData.postal_area,
      state: managerData.state,
      username: managerData.username
    };
  }
};

export default manager;
